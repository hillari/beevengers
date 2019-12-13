from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    """This class creates a better UI for the blog post dashboard"""
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'body', 'category', 'blog_image')
        }),
        ('Advanced options', {  # Create an expandable list for advanced options
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )

    list_display = ('title', 'date_posted', 'author')  # Adds display fields to admin page
    list_filter = ('date_posted',)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Post, PostAdmin)  # first argument needs to be the class from the model
