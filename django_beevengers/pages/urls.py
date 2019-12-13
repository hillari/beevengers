from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
    path('home/', views.Homepage.as_view(), name='homepage'),
    path('calendar/', views.calendar, name='calendar'),
    path('education/', views.education, name='education'),
]