from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'flag_game/post_list.html', {'posts': posts})

def blog(request):
    posts = Post.objects.all().order_by('-published_date')  # последние сверху
    return render(request, 'flag_game/blog.html', {'posts': posts})

def post_detail(request, post_id):
    from django.shortcuts import get_object_or_404
    
    post = get_object_or_404(Post, id=post_id)
    # Похожие посты (по категории или по тегам)
    related_posts = Post.objects.exclude(id=post_id).order_by('?')[:3]
    
    return render(request, 'flag_game/post_detail.html', {
        'post': post,
        'related_posts': related_posts
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    
    return render(request, 'flag_game/register.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    
    return render(request, 'flag_game/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
    else:
        form = LoginForm()
    
    return render(request, 'flag_game/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')