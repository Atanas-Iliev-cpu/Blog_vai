from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog_vai.blogs.forms import BlogCreateForm, BlogEditForm
from blog_vai.blogs.models import Blog
from blog_vai.comments.forms import CommentForm
from blog_vai.comments.models import Comment


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'Blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog = context['Blog']
        # blog = Blog
        if not blog.blog_image:
            blog.blog_image = 'defaults/blog_default.png'


        is_owner = blog.user == self.request.user
        context['comment_form'] = CommentForm(
            initial={
                'blog_pk': self.object.id,
            }
        )
        context['comments'] = blog.comment_set.all()
        context['is_owner'] = is_owner

        return context


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('index')


class BlogEditView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blogs/blog_edit.html'
    form_class = BlogEditForm
    success_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     blog = Blog.objects.get(pk=self.request.user.id)
    #     blog.blog_image = form.cleaned_data['blog_image']
    #     blog.save()
    #     return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_blogs = Blog.objects.all()
        latest_blog = Blog.objects.latest('id')

        if not latest_blog.blog_image:
            latest_blog.blog_image = 'defaults/blog_default.png'
            latest_blog.save()

        for blog in all_blogs:
            if not blog.blog_image:
                blog.blog_image = 'defaults/blog_default.png'
                blog.save()

        context['latest_blog'] = latest_blog
        context['even_blogs'] = [all_blogs[i] for i in range(len(all_blogs)) if
                                 all_blogs[i].title != latest_blog.title and i % 2 == 0]
        context['odd_blog'] = [all_blogs[i] for i in range(len(all_blogs)) if
                               all_blogs[i].title != latest_blog.title and i % 2 != 0]


        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogCreateForm
    # fields = ('title', 'theme', 'description')
    success_url = reverse_lazy('index')
    template_name = 'blogs/blog_create.html'

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

        return redirect('detail blog', blog.id)

    def form_invalid(self, form):
        pass


class SearchBlogView(ListView):
    template_name = 'blogs/searched_blogs.html'
    model = Blog

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list
