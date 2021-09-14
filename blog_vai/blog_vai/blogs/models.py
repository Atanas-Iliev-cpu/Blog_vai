from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Blog(models.Model):
    blog_image = models.ImageField(
        upload_to='blogs',
        blank=True,
        default='defaults/blog_default.png'
    )

    title = models.CharField(
        max_length=50,
    )

    category = models.CharField(
        max_length=50
    )

    description = models.TextField()

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
