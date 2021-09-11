from django.contrib.auth import get_user_model
from django.db import models

from blog_vai.blogs.models import Blog

UserModel = get_user_model()


class Comment(models.Model):

    text = models.TextField(
        max_length=500,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
