from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)

    class Meta:
        # A meta option for Category model representing plural
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
                               )  # AUTH_USER_MODEL b/c we want to use our custom user admin
    date_posted = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    body = models.TextField()
    category = models.ManyToManyField(Category)  # b/c blog can have many category types
    blog_image = models.ImageField(upload_to='images/blog_images', null=True, blank=True)

    class Meta:
        # meta option to tell django how to sort instances
        ordering = ['date_posted']

    def __str__(self):
        return self.title
