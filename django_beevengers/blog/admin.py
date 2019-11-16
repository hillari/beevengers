from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    """This class creates a better UI for the blog post dashboard"""

    list_display = ('title', 'date_posted', 'author')
    list_filter = ('date_posted',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    #
    # TODO figure out how to add 'go back' button in change form
    # def response_change(self, request, object):
    #     if "_go-back" in request.POST:
    #         return HttpResponseRedirect(".")

admin.site.register(Category)
admin.site.register(Post, PostAdmin)  # first argument needs to be the class from the model
