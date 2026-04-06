"""Административная панель для приложения flag_game."""

from django.contrib import admin
from .models import Post

admin.site.register(Post)