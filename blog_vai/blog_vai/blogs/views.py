from django.shortcuts import render
from django.views.generic import ListView, CreateView

from blog_vai.blogs.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'shared/base.html'
    # template_name = 'index.html'


class CreateBlogView(CreateView):
    pass