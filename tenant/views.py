from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.db.models import Func, F

from landlord.models import House
from authentication.models import Tenant
from .models import Match

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
        print(values)
        try: 
            new_tenant = Tenant.objects.filter(user=request.user)
            new_tenant.update(**values)
            new_tenant.first().save()
        except ValidationError as e: 
            print(e.message_dict)

        return redirect('tenant:matches')

    return render(request, 'tenant/profile.html', {"tenant": tenant})

def matches(request):
    tenant = Tenant.objects.filter(user=request.user).first()
    budget = tenant.budget
    houses = House.objects.\
        filter(price__lte=budget+budget*0.2)\
        .annotate(diff=Func(F('price') - budget, function="ABS"))\
        .order_by('diff')
    
    other_tenant = Tenant.objects\
        .exclude(user=request.user)\
        .order_by('?')\
        \
        .first()

    return render(request, 'tenant/matches.html', {'houses': houses, 'other_tenant': other_tenant})

def housing(request):
    return render(request, 'tenant/housing.html')

def view_house(request, house_id):
    house = House.objects.filter(house_id=house_id).first()
    landlord = house.landlord
    other_houses = House.objects.filter(landlord=landlord).exclude(house_id=house_id).order_by('?')[:3]

    if not house: 
        return redirect('tenant:matches')

    return render(request, 'tenant/view_house.html', {'house': house, 'other_houses': other_houses})