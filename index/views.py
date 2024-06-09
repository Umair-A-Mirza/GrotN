from django.shortcuts import render, redirect

from authentication.models import Landlord
from landlord.models import House

# Create your views here.

def index(request): 
    webads = Landlord.objects.filter(user__username="webads").first()
    featured_houses = House.objects.filter(landlord=webads).exclude(address="Jacob Burggraafstraat 144")[:6]

    if not request.user.is_authenticated:
        return render(request, 'index/index.html', {'featured_houses': featured_houses})
    elif 'force' in request.GET: 
        print("Main pageee")
        return render(request, 'index/index.html', {'featured_houses': featured_houses})
    
    if request.user.first_name == "landlord": 
        return redirect('landlord:houses')
    elif request.user.first_name == "tenant":
        return redirect('tenant:matches')

    return render(request, 'index/index.html', {'featured_houses': featured_houses})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tos(request):
    return render(request, 'tos.html')

def custom_404(request, exception=None):
    return render(request, '404.html', {}, status=404)
