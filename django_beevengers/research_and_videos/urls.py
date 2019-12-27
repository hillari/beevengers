from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('recommended_publications/', views.recommended_publications, name='recommended_publications'),
    path('videos/', views.videos, name='videos'),
]
