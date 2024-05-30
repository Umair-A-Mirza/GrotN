from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Tenant, Landlord

# Create your views here.

def tenant_signin(request): 
    if request.method == 'POST': 
        data = request.POST
        print(data)
        user = authenticate(username=data.get("email", ""), password=data.get("password", ""))
        if user is not None: 
            login(request, user)
            return redirect('/')
        else: 
            print("Invalid credentials")
            return redirect('/', message='Invalid Credentials for Tenant Signin.')
        
    return redirect('/', message='Open Tenant Signin Page.')

def tenant_register(request): 
    if request.method == 'POST': 
        data = request.POST
        user = User.objects.create_user(username=data.get("email", ""),
                                        email=data.get("email", ""), 
                                        password=data.get("password", ""),
                                        first_name="tenant")

        tenant = Tenant(
            user=user, 
            fullName=data.get("name", ""),
            phoneNumber=data.get("phone", ""),
            budget=data.get("budget", ""),
            desiredLocation=data.get("address", ""),
            roommate=True if data.get("roommate", False)=="yes" else False
        )
        
        user.save()
        tenant.save()
        login(request, user)
        return redirect('/')

    return redirect('/', message='Open Tenant Register Page.')


def landlord_signin(request): 
    if request.method == 'POST': 
        data = request.POST
        user = authenticate(username=data.get("email", ""), password=data.get("password", ""))
        if user is not None: 
            login(request, user)
            return redirect('/')
        else: 
            print("Invalid credentials")
            return redirect('/', message='Invalid Credentials for Landlord Signin.')

    return redirect('/', message='Open Landlord Signin Page.')

def landlord_register(request): 
    if request.method == 'POST': 
        data = request.POST
        user = User.objects.create_user(username=data.get("email", ""),
                                        email=data.get("email", ""), 
                                        password=data.get("password", ""),
                                        first_name="landlord")
        landlord = Landlord(
            user=user, 
            fullName=data.get("name", ""),
            phoneNumber=data.get("phone", ""),
            noHouses=data.get("houses", "")
        )

        print(f"\n\nLandlord: {landlord}\n\n")
        
        user.save()
        landlord.save()
        login(request, user)
        return redirect('/')

    return redirect('/', message='Open Landlord Register Page.')


def signout(request): 
    logout(request)
    return redirect('/')