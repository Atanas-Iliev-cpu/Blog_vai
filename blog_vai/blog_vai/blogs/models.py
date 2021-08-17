from django.db import models


class Blog(models.Model):

    title = models.CharField(
        max_length=50,
    )

    theme = models.CharField(
        max_length=50
    )

    description = models.TextField()

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    # image_url = models.URLField()
    # image = models.ImageField(
    #     upload_to= 'pets'
    # )

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )
