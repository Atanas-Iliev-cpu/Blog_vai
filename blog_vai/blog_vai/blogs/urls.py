from django.urls import path

from blog_vai.blogs.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    # path('create/', BlogListView.as_view(), name='index'),
]
