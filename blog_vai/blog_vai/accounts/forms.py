from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email']


class LogInForm(AuthenticationForm):
    user = None
    username = forms.CharField(
        max_length=50,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )
    #
    # def clean_password(self):
    #     self.user = authenticate(
    #         username=self.cleaned_data['username'],
    #         password=self.cleaned_data['password'],
    #     )
    #
    #     if not self.user:
    #         raise ValidationError('Incorrect username or password')
    #
    # def save(self):
    #     return self.user
