"""Конфигурация приложения flag_game."""

from django.apps import AppConfig


class FlagGameConfig(AppConfig):
    """Конфигурация для приложения с игрой "Веселье с флагами"."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flag_game'