from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog/', views.blog, name='blog'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
]

urlpatterns = [
    path('', views.post_list, name='home'),
    # path('game/', views.game, name='game'),
    path('blog/', views.blog, name='blog'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]