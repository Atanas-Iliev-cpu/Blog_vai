from django.contrib import admin

from blog_vai.blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass
