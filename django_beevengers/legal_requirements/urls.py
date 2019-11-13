from django.urls import path
from . import views

urlpatterns = [
    path('state_of_alaska/', views.state_of_alaska, name='state_of_alaska'),
    path('municipality_of_anchorage/', views.municipality_of_anchorage, name='municipality_of_anchorage'),

]