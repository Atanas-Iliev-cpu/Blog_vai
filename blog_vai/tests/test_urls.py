from django.test import SimpleTestCase
from django.urls import reverse, resolve

from blog_vai.accounts.views import RegisterView, LogInView, logout_user, ProfileDetailsView, UsersListView, \
    ProfileEditView, MyAllBlogsView, FavBlogsListView, AccountDeleteView
from blog_vai.blogs.views import BlogListView, BlogCreateView, BlogDetailView, BlogEditView, BlogDeleteView, \
    BlogCommentView
from blog_vai.comments.views import CommentDeleteView


class TestBlogUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, BlogListView)

    def test_create_blog_url_resolves(self):
        url = reverse('create blog')
        self.assertEquals(resolve(url).func.view_class, BlogCreateView)

    def test_details_blog_url_resolves(self):
        url = reverse('details blog', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogDetailView)

    def test_edit_blog_url_resolves(self):
        url = reverse('edit blog', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogEditView)

    def test_delete_blog_url_resolves(self):
        url = reverse('delete blog', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogDeleteView)

    def test_comment_blog_url_resolves(self):
        url = reverse('comment blog', args=[1])
        self.assertEquals(resolve(url).func.view_class, BlogCommentView)


class TestAccountUrls(SimpleTestCase):

    def test_register_user_url_resolves(self):
        url = reverse('register user')
        self.assertEquals(resolve(url).func.view_class, RegisterView)

    def test_login_user_url_resolves(self):
        url = reverse('login user')
        self.assertEquals(resolve(url).func.view_class, LogInView)

    def test_logout_user_user_url_resolves(self):
        url = reverse('logout user')
        self.assertEquals(resolve(url).func, logout_user)

    def test_profile_details_user_url_resolves(self):
        url = reverse('profile details')
        self.assertEquals(resolve(url).func.view_class, ProfileDetailsView)

    def test_all_users_user_url_resolves(self):
        url = reverse('all users')
        self.assertEquals(resolve(url).func.view_class, UsersListView)

    def test_profile_edit_blog_url_resolves(self):
        url = reverse('profile edit', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProfileEditView)

    def test_my_blogs_url_resolves(self):
        url = reverse('my blogs', args=[1])
        self.assertEquals(resolve(url).func.view_class, MyAllBlogsView)

    def test_fav_blog_url_resolves(self):
        url = reverse('fav blogs', args=[1])
        self.assertEquals(resolve(url).func.view_class, FavBlogsListView)

    def test_delete_account_url_resolves(self):
        url = reverse('delete account', args=[1])
        self.assertEquals(resolve(url).func.view_class, AccountDeleteView)


class TestCommentUrls(SimpleTestCase):

    def test_register_user_url_resolves(self):
        url = reverse('delete comment', args=[1])
        self.assertEquals(resolve(url).func.view_class, CommentDeleteView)
