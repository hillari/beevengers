from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
    path('home/', views.homepage, name='homepage'),
    path('calendar/', views.calendar, name='calendar'),
    path('different_bees/', views.different_bees, name='different_bees'),
    path('education/', views.education, name='education'),
    path('recommended_sites/', views.recommended_sites, name='recommended_sites'),
    path('legal/', views.legal, name='legal'),
    path('community/', views.community, name='community'),
]