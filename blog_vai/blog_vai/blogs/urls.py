from django.urls import path

from blog_vai.blogs.views import BlogListView, BlogCreateView, BlogDetailView, BlogCommentView, BlogEditView, \
    BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('create/', BlogCreateView.as_view(), name='create blog'),
    path('details/<int:pk>', BlogDetailView.as_view(), name='details blog'),
    path('edit/<int:pk>', BlogEditView.as_view(), name='edit blog'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete blog'),
    path('comments/<int:pk>', BlogCommentView.as_view(), name='comment blog'),
]
