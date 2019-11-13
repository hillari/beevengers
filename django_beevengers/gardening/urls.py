from django.urls import path
from . import views

urlpatterns = [
    path('pollinator_friendly_vegetation/', views.pollinator_friendly_vegetation, name='pollinator_friendly_vegetation'),

]
