from django.urls import path
from . import views

app_name = 'landlord'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('houses/', views.houses, name='houses'),
    path('matches/', views.matches, name='matches'),
    path('house/<int:house_id>/', views.edit_house, name='edit_house'),
    path('house/new/', views.new_house, name='new')
]