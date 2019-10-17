from django.db import models

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    # Fields that define a blog post. Note, order of these define how they render on admin page
    title = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    body = models.TextField()

# TODO add this back in after we create the view
    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of the model."""
    #     return reverse('model-detail-view', args=[str(self.id)])

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        # This string uses the title field to represent each post object
        return self.title




