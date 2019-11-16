from django.shortcuts import render
from .models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-date_posted')  # status 1 = only show published posts at top
    template_name = 'pages/blog/blog_index.html'
    # should we add  pagination?


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'pages/blog/blog_detail.html'
