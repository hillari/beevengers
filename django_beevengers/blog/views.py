from .models import Post
from django.views import generic


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-date_posted')
    template_name = 'pages/blog/blog_index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'pages/blog/blog_detail.html'
