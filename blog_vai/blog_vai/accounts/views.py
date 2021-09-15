from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView, ListView, DeleteView, UpdateView
from blog_vai.accounts.forms import RegisterForm, LogInForm, ProfileForm
from blog_vai.accounts.models import Profile
from blog_vai.blogs.models import Blog
from blog_vai.comments.models import Comment

UserModel = get_user_model()


class ProfileEditView(FormView, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    success_url = reverse_lazy('profile details')

    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.request.user.id)
        profile.profile_image = form.cleaned_data['profile_image']
        profile.save()
        return super().form_valid(form)


class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/delete_account.html'
    success_url = reverse_lazy('index')


class ProfileDetailsView(LoginRequiredMixin, FormView):
    form_class = ProfileForm
    template_name = 'accounts/your_profile.html'
    success_url = reverse_lazy('profile details')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.id)
        user_blogs = Blog.objects.filter(user_id=self.request.user.id)
        comments = Comment.objects.filter(user_id=self.request.user.id)
        comment_blogs = Comment.objects.filter(user_id=self.request.user.id).distinct('blog_id')

        if not profile.profile_image:
            profile.profile_image = 'defaults/profile_default.png'
            profile.save()

        context['blogs_cnt'] = len(user_blogs)
        context['profile'] = profile
        context['comments_cnt'] = len(comments)
        # context['comment_blogs'] = comment_blogs

        return context


def user_details(request, pk):
    user = UserModel.objects.get(pk=pk)

    context = {
        'user': user,
        'blogs': user.blog_set.all(),
        'blogs_cnt': len(user.blog_set.all()),
        'comments': user.comment_set.all(),
        'comments_cnt': len(user.comment_set.all()),
        'profile': user.profile,
        # 'comment_blogs': Comment.objects.filter(user_id=user.id).distinct('blog_id'),
    }

    return render(request, 'accounts/user_profile.html', context)


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
    template_name = 'accounts/all_users.html'


class MyAllBlogsView(ListView):
    model = UserModel
    template_name = 'accounts/my_blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_blogs = Blog.objects.filter(user_id=self.request.user.id)

        context['blogs'] = user_blogs

        return context


class FavBlogsListView(ListView):
    model = UserModel
    template_name = 'accounts/fav_blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_blogs = Blog.objects.filter(user_id=self.request.user.id)
        comments = Comment.objects.filter(user_id=self.request.user.id).distinct('blog_id')

        context['comments'] = comments

        return context
