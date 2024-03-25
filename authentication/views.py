from django.shortcuts import render

# Create your views here.

def user_signin(request): 
    return render(request, 'auth/user-signin.html')

def user_register(request): 
    return render(request, 'auth/user-register.html')

def landlord_signin(request): 
    return render(request, 'auth/landlord-signin.html')

def landlord_register(request): 
    return render(request, 'auth/landlord-register.html')