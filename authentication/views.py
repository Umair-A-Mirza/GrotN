from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Tenant, Landlord

# Create your views here.

def tenant_signin(request): 
    print("Tenant sign in")
    if request.method == 'POST': 
        data = request.POST
        user = authenticate(username=data.get("email", ""), password=data.get("password", ""))
        if user is not None: 
            login(request, user)
            return redirect('/')
        else: 
            print("Invalid credentials")
            return render(request, 'auth/tenant-signin.html')
        
    return render(request, 'auth/tenant-signin.html')

def tenant_register(request): 
    if request.method == 'POST': 
        data = request.POST
        user = User.objects.create_user(username=data.get("email", ""),
                                        email=data.get("email", ""), 
                                        password=data.get("password", ""),
                                        first_name="tenant")
        tenant = Tenant(user=user)
        
        user.save()
        tenant.save()
        login(request, user)
        return redirect('/')

    return render(request, 'auth/tenant-register.html')



def landlord_signin(request): 
    if request.method == 'POST': 
        data = request.POST
        user = authenticate(username=data.get("email", ""), password=data.get("password", ""))
        if user is not None: 
            login(request, user)
            return redirect('/')
        else: 
            print("Invalid credentials")
            return render(request, 'auth/landlord-signin.html')

    return render(request, 'auth/landlord-signin.html')

def landlord_register(request): 
    if request.method == 'POST': 
        data = request.POST
        user = User.objects.create_user(username=data.get("email", ""),
                                        email=data.get("email", ""), 
                                        password=data.get("password", ""),
                                        first_name="landlord")
        landlord = Landlord(user=user)
        
        user.save()
        landlord.save()
        login(request, user)
        return redirect('/')

    return render(request, 'auth/landlord-register.html')

def signout(request): 
    logout(request)
    return redirect('/')