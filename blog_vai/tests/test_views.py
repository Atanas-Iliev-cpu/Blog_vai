from django.urls import reverse
from django.test import TestCase, Client

from blog_vai.accounts.models import SiteUser
from blog_vai.blogs.models import Blog
from blog_vai.comments.models import Comment


class TestViews(TestCase):

    def setUp(self):
        self.user1 = SiteUser.objects.create(
            email='nasko@iliev.it',
            is_staff=True,
            date_joined='2021-08-20 19:45:07.309937 +00:00',
        )
        self.blog1 = Blog.objects.create(
            title='Title1',
            theme='Theme1',
            description='Description1',
            date_joined='2021-08-20 19:45:07.309937 +00:00',
            user=self.user1,
        )
        self.comment1 = Comment.objects.create(
            text='test comment',
            blog=self.blog1,
            user=self.user1,
        )

        self.client = Client()
        self.list_url = reverse('index')
        self.detail_url = reverse('detail blog', args=[self.blog1.id])
        self.create_url = reverse('create blog')
        self.edit_url = reverse('edit blog', args=[self.blog1.id])
        self.delete_url = reverse('delete blog', args=[self.blog1.id])
        self.comment_url = reverse('delete comment', args=[self.comment1.id])

    def test_blog_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_blog_detail_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_detail.html')

    def test_blog_create_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_create.html')

    def test_blog_edit_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.edit_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_edit.html')

    def test_blog_delete_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_delete.html')

    def test_comment_delete_GET(self):
        self.client.force_login(self.user1)
        response = self.client.get(self.comment_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'comments/demo_comment_delete.html')

    def test_blog_create_POST(self):
        self.client.force_login(self.user1)
        response = self.client.post(self.create_url, {
            'title': 'test title',
            'theme': 'test theme',
            'description': 'test desc',
            'user': self.user1,
        })

        self.assertEqual(response.status_code, 302)
        blog = Blog.objects.filter(title__icontains='test title')[0]
        self.assertEquals(blog.title, 'test title')
        self.assertEquals(blog.theme, 'test theme')
        self.assertEquals(blog.description, 'test desc')
        self.assertEquals(blog.user, self.user1)

