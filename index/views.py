from django.shortcuts import render, redirect

# Create your views here.

def index(request): 
    if not request.user.is_authenticated:
        return render(request, 'index/index.html')
    
    if request.user.first_name == "landlord": 
        return redirect('landlord:houses')
    elif request.user.first_name == "tenant":
        return redirect('tenant:matches')

    return redirect('/')