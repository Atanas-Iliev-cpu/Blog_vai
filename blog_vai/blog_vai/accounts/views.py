from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from blog_vai.accounts.forms import RegisterForm, LogInForm

UserModel = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    model = UserModel
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     login(self.request, self.object)
    #     return result


class LogInView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LogInForm

    def get_success_url(self):
        return reverse('index')


def logout_user(request):
    logout(request)
    return redirect('index')
