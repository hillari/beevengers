from . import views
from django.urls import path

urlpatterns = [
    # The name= part is what gets referenced in the html
    path('', views.PostList.as_view(), name='blog-home'),  # localhost/blog
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]
