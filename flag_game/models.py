"""Модели данных для приложения flag_game."""

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Модель поста в блоге о флагах."""

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Опубликовать пост (установить дату публикации)."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Возвращает строковое представление поста."""
        return str(self.title)