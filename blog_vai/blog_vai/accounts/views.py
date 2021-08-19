from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, ListView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from blog_vai.accounts.forms import RegisterForm, LogInForm, ProfileForm
from blog_vai.accounts.models import Profile
from blog_vai.blogs.models import Blog
from blog_vai.comments.models import Comment

UserModel = get_user_model()


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete_account.html'
    success_url = reverse_lazy('index')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    form_class = ProfileForm
    template_name = 'accounts/user_profile.html'
    success_url = reverse_lazy('profile details')

    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.request.user.id)
        profile.profile_image = form.cleaned_data['profile_image']
        profile.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.id)
        user_blogs = Blog.objects.filter(user_id=self.request.user.id)
        comments = Comment.objects.filter(user_id=self.request.user.id)

        context['blogs'] = user_blogs
        context['profile'] = profile
        context['comments'] = comments

        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    model = UserModel
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LogInView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LogInForm

    def get_success_url(self):
        return reverse('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class UsersListView(ListView):
    model = UserModel
    # template_name = 'shared/base.html'
    template_name = 'accounts/demo_all_users.html'


class MyAllBlogsView(ListView):
    model = UserModel
    template_name = 'accounts/my_blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # profile = Profile.objects.get(pk=self.request.user.id)
        user_blogs = Blog.objects.filter(user_id=self.request.user.id)
        # comments = Comment.objects.filter(user_id=self.request.user.id)

        context['blogs'] = user_blogs
        # context['profile'] = profile
        # context['comments'] = comments

        return context

    # object = None
    # # paginate_by = 3
    # #
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object(queryset=Blog.objects.all())
    #     return super().get(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['blogs'] = self.object
    #     return context
    #
    # def get_queryset(self):
    #     return self.object.article_set.all()


class FavBlogsListView(ListView):
    model = UserModel
    template_name = 'accounts/fav_blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # profile = Profile.objects.get(pk=self.request.user.id)
        # user_blogs = Blog.objects.filter(user_id=self.request.user.id)
        # fav_blogs = Blog.objects.filter(user_id=self.request.user.id)
        comments = Comment.objects.filter(user_id=self.request.user.id)

        # context['blogs'] = user_blogs
        # context['profile'] = profile
        context['comments'] = comments

        return context
