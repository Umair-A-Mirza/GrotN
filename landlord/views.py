from django.shortcuts import render

from .models import House

# Create your views here.

def profile(request):
    return render(request, 'landlord/profile.html')

def houses(request):
    return render(request, 'landlord/houses.html')  

def matches(request):
    return render(request, 'landlord/matches.html')

def edit_house(request, house_id):
    house = House.objects.filter(house_id=house_id).first()
    return render(request, 'landlord/edit_house.html', {'house': house})

def new_house(request): 
    return render(request, 'landlord/new_house.html')