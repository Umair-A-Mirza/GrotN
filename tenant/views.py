from django.shortcuts import render
from landlord.models import House  

# Create your views here.

def profile(request):
    return render(request, 'tenant/profile.html')

def matches(request):
    return render(request, 'tenant/matches.html')

def housing(request):
    return render(request, 'tenant/housing.html')

def view_house(request, house_id):
    house = House.objects.filter(house_id=house_id).first()
    return render(request, 'tenant/view_house.html', {'house': house})