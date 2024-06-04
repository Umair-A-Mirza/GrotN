from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.db.models import Func, F

from landlord.models import House
from authentication.models import Tenant
from .models import Swipe

# Create your views here.

def profile(request):
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
        if not roommate:
            existing_swipes = Swipe.objects.filter(tenant=tenant)
            for existing_swipe in existing_swipes:
                existing_swipe.active = False
                existing_swipe.save()
            
            match = Swipe(tenant=tenant, partner=None, status=True)
            match.save()
        else: 
            match = Swipe.objects.filter(tenant=tenant, partner=None).first()
            if match: 
                match.delete()

        return redirect('tenant:matches')

    return render(request, 'tenant/profile.html', {"tenant": tenant})

def matches(request):
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
        # TODO: based on the old and current swipe, update the match!
        partner_id = request.POST.get('partner_id')
        partner = Tenant.objects.filter(id=partner_id).first()

        existing_swipe = Swipe.objects.filter(tenant=tenant, partner=partner).first()
        if existing_swipe: 
            existing_swipe.status = "shortlist" in request.POST
            existing_swipe.active = True
            existing_swipe.save()
            return redirect('tenant:matches')
        
        # if match doesn't exist, create a new one
        swipe = Swipe(tenant=tenant, partner=partner, status="shortlist" in request.POST)
        swipe.save()
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
        print(other_tenant)
        match = Swipe.objects.filter(tenant=tenant, partner=other_tenant).first()
        print(match)
        if not match or not match.active: 
            return render(request, 'tenant/matches.html', {'houses': houses, 'other_tenant': other_tenant})

    return render(request, 'tenant/matches.html', {'houses': houses, 'tenant': tenant})

def housing(request):
    return render(request, 'tenant/housing.html')

def view_house(request, house_id):
    house = House.objects.filter(house_id=house_id).first()
    landlord = house.landlord
    other_houses = House.objects.filter(landlord=landlord).exclude(house_id=house_id).order_by('?')[:3]

    if not house: 
        return redirect('tenant:matches')

    return render(request, 'tenant/view_house.html', {'house': house, 'other_houses': other_houses})