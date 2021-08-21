from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from blog_vai.accounts.models import Profile

UserModel = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'first_name', 'last_name', 'phone_number')


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email']


class LogInForm(AuthenticationForm):
    error_messages = {
        'invalid_login': (
            "Please enter a correct E-mail address and password."
            " This fields are case-sensitive."
        )}

