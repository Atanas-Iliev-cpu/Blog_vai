from django.urls import path

from blog_vai.comments.views import CommentDeleteView

urlpatterns = (
    path('delete_comment/<int:pk>', CommentDeleteView.as_view(), name='delete comment'),
)
