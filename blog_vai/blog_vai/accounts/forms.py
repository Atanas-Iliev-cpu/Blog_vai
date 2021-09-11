from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

from blog_vai.accounts.models import Profile

UserModel = get_user_model()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image', 'first_name', 'last_name', 'phone_number')
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('profile_image', css_class='form-control mb-4')
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-2'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'phone_number',
            Submit('submit', 'Update', css_class='mt-3' )
        )


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
