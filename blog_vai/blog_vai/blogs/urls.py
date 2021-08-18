from django.urls import path

from blog_vai.blogs.views import BlogListView, CreateBlogView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('create/', CreateBlogView.as_view(), name='create blog'),
    path('details/<int:pk>', BlogDetailView.as_view(), name='details blog'),
]
