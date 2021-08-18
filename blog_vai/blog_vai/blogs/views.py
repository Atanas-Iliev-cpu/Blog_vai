from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, FormView, UpdateView, DeleteView

from blog_vai.blogs.models import Blog
from blog_vai.comments.forms import CommentForm
from blog_vai.comments.models import Comment


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/demo_blog_delete.html'
    success_url = reverse_lazy('index')


class BlogEditView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blogs/demo_blog_edit.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('index')


class BlogDetailView(DetailView):
    model = Blog
    # template_name = 'blogs/detail-blog.html'
    template_name = 'blogs/demo_blog_detail.html'
    context_object_name = 'Blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = context['Blog']

        # blog.likes_count = blog.like_set.count()
        is_owner = blog.user == self.request.user

        # is_liked_by_user = blog.like_set.filter(user_id=self.request.user.id) \
        #     .exists()
        context['comment_form'] = CommentForm(
            initial={
                'pet_pk': self.object.id,
            }
        )
        context['comments'] = blog.comment_set.all()
        context['is_owner'] = is_owner
        # context['is_liked'] = is_liked_by_user

        return context


class BlogListView(ListView):
    model = Blog
    # template_name = 'shared/base.html'
    template_name = 'index.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'theme', 'description')
    success_url = reverse_lazy('index')
    template_name = 'blogs/demo_blog_create.html'

    def form_valid(self, form):
        blog = form.save(commit=False)
        blog.user = self.request.user
        blog.save()
        return super().form_valid(form)


class BlogCommentView(LoginRequiredMixin, View):
    form_class = CommentForm
    success_url = ''

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        blog = Blog.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            blog=blog,
            user=self.request.user,
        )
        comment.save()

        return redirect('details blog', blog.id)

    def form_invalid(self, form):
        pass
# @login_required
# def comment_blog(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             text=form.cleaned_data['text'],
#             blog=blog,
#             # user=self.request.user,
#         )
#         comment.save()
#
#     return redirect('details blog', blog.id)
