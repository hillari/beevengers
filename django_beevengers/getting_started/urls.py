from django.urls import path
from . import views

urlpatterns = [
    path('different_honey_bees/', views.different_honey_bees, name='different_honey_bees'),
    path('different_hives/', views.different_hives, name='different_hives'),
    path('recommended_equipment/', views.recommended_equipment, name='recommended_equipment'),
    path('hive_placement/', views.hive_placement, name='hive_placement'),
    path('classes/', views.classes, name='classes'),
]

