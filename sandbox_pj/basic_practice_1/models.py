from django.db import models


class Posting(models.Model):
    message = models.CharField(
        max_length=140,
        verbose_name='やること')

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='日時')
