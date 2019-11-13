from django.urls import path
from . import views

urlpatterns = [
    path('suitable_hives/', views.suitable_hives, name='suitable_hives'),
    path('colony_analysis/', views.colony_analysis, name='colony_analysis'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('honey_bee_health/', views.honey_bee_health, name='honey_bee_health'),
    path('maintenance/', views.maintenance, name='maintenance'),
]