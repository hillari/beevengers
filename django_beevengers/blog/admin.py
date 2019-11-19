from django.contrib import admin
# from django.http import HttpResponseRedirect

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    """This class creates a better UI for the blog post dashboard"""

    list_display = ('title', 'date_posted', 'author')
    list_filter = ('date_posted',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}

    # TODO figure out how to add 'go back' button in change form
    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     extra_context = extra_context or self.extra_context()
    #     return super(PostAdmin, self).change_view(
    #         request, object_id, form_url, extra_context=extra_context,
    #     )

admin.site.register(Category)
admin.site.register(Post, PostAdmin)  # first argument needs to be the class from the model
