from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'tenant/profile.html')

def matches(request):
    return render(request, 'tenant/matches.html')

def housing(request):
    return render(request, 'tenant/housing.html')