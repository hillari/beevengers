from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    """This class creates a better UI for the blog post dashboard"""
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'body', 'category', 'blog_image')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )

    # list_display = ('title', 'date_posted', 'author')
    list_filter = ('date_posted',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    # exclude = ('slug', 'date_modified')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)  # first argument needs to be the class from the model
