from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('calendar/', views.calendar, name='calendar'),
    path('different_bees/', views.different_bees, name='different_bees'),
    path('education/', views.education, name='education'),
    path('recommended_sites/', views.recommended_sites, name='recommended_sites'),
]