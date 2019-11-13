from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('recommended_publications/', views.recommended_publications, name='recommended_publications'),
    path('recommended_sites/', views.recommended_sites, name='recommended_sites'),
    path('videos/', views.videos, name='videos'),
]
