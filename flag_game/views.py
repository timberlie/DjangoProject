from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'flag_game/post_list.html', {'posts': posts})

def blog(request):
    posts = Post.objects.all().order_by('-published_date')  # последние сверху
    return render(request, 'flag_game/blog.html', {'posts': posts})