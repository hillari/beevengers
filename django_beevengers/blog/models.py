from django.db import models
from django.conf import settings

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    #                            )  # AUTH_USER_MODEL b/c we want to use our custom user admin
    date_posted = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    body = models.TextField()
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ['date_posted']  # here we tell django to sort results by date_posted field

    # TODO add this back in after we create the view
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.title
