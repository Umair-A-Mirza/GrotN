from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.db.models import Func, F, Q

from landlord.models import House, Housing
from authentication.models import Tenant
from .models import Swipe, Match

from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt 

from django.contrib.auth.decorators import login_required

import stripe

# Create your views here.

def login(request):
    return render(request, 'tenant/login.html')

def signup(request):
    return render(request, 'tenant/signup.html')

@login_required(login_url='index:index')
def profile(request):
    if "tenant" not in request.user.first_name: 
        return redirect('landlord:houses')
    
    tenant = Tenant.objects.filter(user=request.user).first()

    if request.method == 'POST':
        fullName = request.POST.get('name')
        phoneNumber = request.POST.get('phone')
        budget = request.POST.get('budget')
        desiredCity = request.POST.get('city')
        desiredDistrict = request.POST.get('district')
        roommate = request.POST.get('roommate') == 'yes'
        activities = request.POST.get('activities').strip()
        interests = request.POST.get('interests').strip()
        preferences = request.POST.get('preferences').strip()

        values = {
            'fullName': fullName,
            'phoneNumber': phoneNumber, 
            'budget': budget,
            'desiredCity': desiredCity,
            'desiredDistrict': desiredDistrict,
            'roommate': roommate,
            'activities': activities, 
            'interests': interests, 
            'preferences': preferences
        }
        
        try: 
            new_tenant = Tenant.objects.filter(user=request.user)
            new_tenant.update(**values)
            new_tenant.first().save()
        except ValidationError as e: 
            print(e.message_dict)

        # create a single-person match
        existing_swipes = Swipe.objects.filter(tenant=tenant)
        if not roommate:
            for existing_swipe in existing_swipes:
                existing_swipe.active = existing_swipe.status
                existing_swipe.status = False
                existing_swipe.save()
                # update_match(existing_swipe)
            
            match = Match(tenant1=tenant, tenant2=None, status=True)
            match.save()
        else: 
            for existing_swipe in existing_swipes:
                existing_swipe.status = existing_swipe.active
                existing_swipe.active = True
                existing_swipe.save()
                # update_match(existing_swipe)

            match = Match.objects.filter(tenant1=tenant, tenant2=None).first()
            if match: 
                match.delete()

        return redirect('tenant:matches')

    return render(request, 'tenant/profile.html', {"tenant": tenant})

@login_required(login_url='index:index')
def matches(request):
    if "tenant" not in request.user.first_name: 
        return redirect('landlord:houses')
    
    # Get the logged in tenant and their budget
    tenant = Tenant.objects.filter(user=request.user).first()
    budget = tenant.budget

    if request.method == 'POST':
        # if the user doesn't have any matches left, prompt them to click on 'more'
        # if user clicks on 'more', deactivate 5 of their random matches
        if 'more' in request.POST:
            tenant_swipes = Swipe.objects\
                .filter(tenant=tenant)\
                .order_by('?')[:5]

            for tenant_swipe in tenant_swipes: 
                tenant_swipe.active = False
                tenant_swipe.save()
            return redirect('tenant:matches')
        
        # if user clicks on 'shortlist' or 'reject', update the swipe
        partner_id = request.POST.get('partner_id')
        partner = Tenant.objects.filter(id=partner_id).first()

        existing_swipe = Swipe.objects.filter(tenant=tenant, partner=partner).first()
        if existing_swipe: 
            existing_swipe.status = "shortlist" in request.POST
            existing_swipe.active = True
            existing_swipe.save()
            # new_match = update_match(existing_swipe)
            # print(f"Here is your new match: {new_match}")
            return redirect('tenant:matches')
        
        # if match doesn't exist, create a new one
        swipe = Swipe(tenant=tenant, partner=partner, status="shortlist" in request.POST)
        swipe.save()
        # new_match = update_match(swipe)
        # print(f"Here is your new match: {new_match}")
        return redirect('tenant:matches')


    # Get houses that are within user's budget
    houses = House.objects.\
        filter(price__lte=budget+budget*0.2)\
        .annotate(diff=Func(F('price') - budget, function="ABS"))\
        .order_by('diff')
    
    # Get 5 random tenants
    other_tenants = Tenant.objects\
        .exclude(user=request.user)\
        .order_by('?')[:5] if tenant.roommate else []
    
    # Send one non-active match to the user
    for other_tenant in other_tenants: 
        swipe = Swipe.objects.filter(tenant=tenant, partner=other_tenant).first()
        if not swipe or not swipe.active: 
            return render(request, 'tenant/matches.html', {'houses': houses, 'other_tenant': other_tenant})

    return render(request, 'tenant/matches.html', {'houses': houses, 'tenant': tenant})

@login_required(login_url='index:index')
def housing(request):
    if "tenant" not in request.user.first_name: 
        return redirect('landlord:houses')
    
    housings = Housing.objects.filter(
        Q(tenants__tenant1__user=request.user) | 
        Q(tenants__tenant2__user=request.user),
        approved=True)

    if request.method == 'POST':
        match_id = request.POST.get('id')
        housing = Housing.objects.filter(match_id=match_id).first()
        if 'cancel' in request.POST:
            housing.active = housing.approved
            housing.approved = False
            housing.save()

        print(housing)
        
        return redirect('tenant:housing')

    return render(request, 'tenant/housing.html', {'housings': housings})

# No need to be logged in to view a house
def view_house(request, house_id):
    # landlords can also view a house, so no logic here
    
    house = House.objects.filter(house_id=house_id).first()
    landlord = house.landlord
    other_houses = House.objects.filter(landlord=landlord).exclude(house_id=house_id).order_by('?')[:3]

    if not house: 
        return redirect('tenant:matches')

    return render(request, 'tenant/view_house.html', {'house': house, 'other_houses': other_houses})


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        # PRODUCTION: domain_url = 'https://your-domain.com/'
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items = [
                    {
                        'price': 'price_1POZVAP9S3FmSLqtSAlYdfSx',
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)})
