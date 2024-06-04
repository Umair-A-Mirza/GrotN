from django.shortcuts import render, redirect

# Create your views here.

def index(request): 
    if not request.user.is_authenticated:
        return render(request, 'index/index.html')
    elif 'force' in request.GET: 
        print("Main pageee")
        return render(request, 'index/index.html')
    
    if request.user.first_name == "landlord": 
        return redirect('landlord:houses')
    elif request.user.first_name == "tenant":
        return redirect('tenant:matches')

    return render(request, 'index/index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tos(request):
    return render(request, 'tos.html')

def custom_404(request, exception=None):
    return render(request, '404.html', {}, status=404)
