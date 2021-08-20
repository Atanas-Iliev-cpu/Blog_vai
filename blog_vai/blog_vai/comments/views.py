from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from blog_vai.comments.models import Comment


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comments/demo_comment_delete.html'
    success_url = reverse_lazy('index')
