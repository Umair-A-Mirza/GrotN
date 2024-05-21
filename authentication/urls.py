from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('landlord/signin', views.landlord_signin, name='landlord-signin'),
    path('landlord/register', views.landlord_register, name='landlord-register'),
    path('tenant/signin', views.tenant_signin, name='tenant-signin'),
    path('tenant/register', views.tenant_register, name='tenant-register'),
    path('signout', views.signout, name='signout'),
]