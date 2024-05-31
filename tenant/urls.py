from django.urls import path
from . import views

app_name = 'tenant'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('matches/', views.matches, name='matches'),
    path('housing/', views.housing, name='housing'),
    path('house/<int:house_id>/', views.view_house, name='view_house'),
]