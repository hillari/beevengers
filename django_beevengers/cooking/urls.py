from django.urls import path
from . import views

urlpatterns = [
    path('recipes_with_honey/', views.recipes_with_honey, name='recipes_with_honey'),

]
