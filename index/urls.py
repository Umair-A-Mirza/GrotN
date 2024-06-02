from django.urls import path
from .views import index, about, contact, tos

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('tos/', tos, name='tos'), 
]