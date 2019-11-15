from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]
