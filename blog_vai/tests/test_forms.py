from django.test import SimpleTestCase, TestCase, Client
from django.contrib.auth import get_user_model

from blog_vai.accounts.forms import RegisterForm, LogInForm, ProfileForm
from blog_vai.accounts.models import Profile
from blog_vai.comments.forms import CommentForm

UserModel = get_user_model()


class TestRegisterAndLoginForms(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = UserModel.objects.create_user(
            email='Test@gmail.com',
            password='12345678qwe!',
            # profile=Profile,
        )

    def test_register_form_valid_data(self):
        form = RegisterForm({
            'email': "test@mail.bg",
            'password1': '123456789qwe!',
            'password2': '123456789qwe!',
        })

        self.assertTrue(form.is_valid())

    def test_register_form_no_data(self):
        form = RegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_register_form_password_no_match(self):
        form = RegisterForm({
            'email': "mail@mail.bg",
            'password1': '123456789qwe!',
            'password2': '123456789qw!',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_login_form_form_is_not_valid(self):
        form = LogInForm({

        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_login_form_form_is_not_valid_password(self):
        form = LogInForm({
            'email': 'Test@gmail.com',
            'password': '12345678qw!',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 0)


class TestProfileForm(TestCase):

    def test_profile_with_email_valid(self):
        form = ProfileForm({
            'profile_image': '',
            'email': 'mail@mail.bg',
            'first_name': '',
            'last_name': '',
            'phone_number': ''
        })

        self.assertTrue(form.is_valid())


class TestCommentForm(TestCase):
    def test_comment_form_valid_data(self):
        form = CommentForm(data={
            'text': 'some text'
        })

        self.assertTrue(form.is_valid())

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={
            'text': ''
        })

        self.assertFalse(form.is_valid())
