from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from blog_vai.blogs.models import Blog


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/detail-blog.html'
    context_object_name = 'Blog'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     blog = context['blog']
    #
    #     return context


class BlogListView(ListView):
    model = Blog
    # template_name = 'shared/base.html'
    template_name = 'index.html'


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'theme', 'description')
    success_url = reverse_lazy('index')
    template_name = 'blogs/create-blog.html'

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        return super().form_valid(form)
