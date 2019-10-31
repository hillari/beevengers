from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('', views.redirect_view, name='redirect_view'),
    path('home/', views.homepage, name='homepage'),
    path('store/', views.store, name='store'),
    path('calendar/', views.calendar, name='calendar'),
    path('different_bees/', views.different_bees, name='different_bees'),
    path('education/', views.education, name='education'),
    path('recommended_sites/', views.recommended_sites, name='recommended_sites'),
]