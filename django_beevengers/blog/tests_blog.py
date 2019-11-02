from django.test import TestCase
from .models import Post, Category
from django.contrib.auth import get_user_model


class TestBlogModel(TestCase):

    def test_title(self):
    #   user = get_user_model().objects.create_user('testuser', 'email@email.com', 'password')
        post = Post.objects.create(title="My test title",
                                   body="")
        self.assertEqual(str(post), post.title)
        self.assertEqual(post.title.count(post.title), 1)
