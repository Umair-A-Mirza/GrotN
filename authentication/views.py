from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Tenant, Landlord

# Create your views here.

def tenant_signin(request): 
    request.session["href"] = "#login"
    if request.method == 'POST': 
        data = request.POST
        print(data)
        user = authenticate(username=data.get("email", ""), password=data.get("password", ""))
        if user is None: 
            request.session['message'] = 'Invalid Credentials'
            return redirect('/')
        elif "tenant" not in user.first_name: 
            request.session['message'] = 'Wrong User Type'
            return redirect('/')
        elif "tenant" in user.first_name:
            request.session.pop('message', None)
            request.session.pop('href', None)
            login(request, user)
            return redirect('/')
    
    return redirect('/')

def tenant_register(request): 
    if request.method == 'POST': 
        data = request.POST
        request.session["tenantData"] = dict(data)

        email = data.get("email", "")
        pw1 = data.get("password", "")
        pw2 = data.get("password2", "")

        if pw1 != pw2:
            request.session['message'] = 'Passwords do not match.'
            request.session['href'] = "#createAccount"
            return redirect('/')

        user = User(username=email,
                    email=email, 
                    password=pw1,
                    first_name="tenant")
        

        tenant = Tenant(
            user=user, 
            fullName=data.get("name", ""),
            phoneNumber=data.get("phone", ""),
            budget=data.get("budget", ""),
            desiredCity=data.get("city", ""),
            roommate=True if data.get("roommate", False)=="yes" else False
        )
        
        try: 
            user.save()
            tenant.save()
            login(request, user)
        except Exception as e: 
            print(e)
            request.session['message'] = e
            request.session['href'] = "#createAccount"
            return redirect('/')
        
        # Sucess
        request.session.pop('message', None)
        request.session.pop('href', None)
        request.session.pop('data', None)
        return redirect('/')

    return redirect('/')


def landlord_signin(request): 
    request.session["href"] = "#landlordLogin"
    if request.method == 'POST': 
        data = request.POST
        user = authenticate(username=data.get("email", ""), password=data.get("password", ""))
        if user is None: 
            request.session['message'] = 'Invalid Credentials'
            return redirect('/')
        elif "landlord" not in user.first_name: 
            request.session['message'] = 'Wrong User Type'
            return redirect('/')
        elif "landlord" in user.first_name:
            request.session.pop('message', None)
            request.session.pop('href', None)
            login(request, user)
            return redirect('/')

    return redirect('/')

def landlord_register(request): 
    if request.method == 'POST': 
        data = request.POST
        request.session["landlordData"] = dict(data)

        email = data.get("email", "")
        pw1 = data.get("password", "")
        pw2 = data.get("password2", "")

        if pw1 != pw2:
            request.session['message'] = 'Passwords do not match.'
            request.session['href'] = "#createLandlordAccount"
            return redirect('/')

        user = User(username=email,
                    email=email, 
                    password=pw1,
                    first_name="landlord")

        landlord = Landlord(
            user=user, 
            fullName=data.get("name", ""),
            phoneNumber=data.get("phone", ""),
            noHouses=data.get("houses", ""), 
            baseCity=data.get("city", "")
        )

        try: 
            user.save()
            landlord.save()
            login(request, user)
        except Exception as e:
            request.session['message'] = e
            request.session['href'] = "#createLandlordAccount"
            return redirect('/')

        # Sucess
        request.session.pop('message', None)
        request.session.pop('href', None)
        request.session.pop('data', None)
        return redirect('/')

    return redirect('/')


def signout(request): 
    logout(request)
    return redirect('/')