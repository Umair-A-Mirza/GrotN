from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('landlord/signin', views.landlord_signin, name='landlord-signin'),
    path('landlord/register', views.landlord_register, name='landlord-register'),
    path('user/signin', views.user_signin, name='user-signin'),
    path('user/register', views.user_register, name='user-register'),
]