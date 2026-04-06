"""URL-маршруты для приложения flag_game."""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='home'),
    path('game/', views.game, name='game'),
    path('api/get_question/', views.get_question, name='get_question'),
    path('api/check_answer/', views.check_answer, name='check_answer'),
    path('blog/', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]