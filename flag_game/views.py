"""View-функции для приложения flag_game."""

import random
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from .models import Post
from .forms import RegistrationForm, LoginForm
from .flags_data import FLAGS_DATABASE, get_random_flags, get_country_by_id


def post_list(request):
    """
    Отображает главную страницу со списком последних постов.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Страница со списком постов.
    """
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('published_date')
    return render(request, 'flag_game/post_list.html', {'posts': posts})


def blog(request):
    """
    Отображает страницу блога со всеми постами.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Страница блога со списком постов.
    """
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'flag_game/blog.html', {'posts': posts})


def post_detail(request, post_id):
    """
    Отображает детальную страницу отдельного поста.

    Args:
        request: HTTP-запрос.
        post_id: ID поста.

    Returns:
        HttpResponse: Страница с полным текстом поста.
    """
    post = get_object_or_404(Post, id=post_id)
    related_posts = Post.objects.exclude(id=post_id).order_by('?')[:3]

    return render(request, 'flag_game/post_detail.html', {
        'post': post,
        'related_posts': related_posts
    })


def register(request):
    """
    Регистрация нового пользователя.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Страница регистрации или редирект на главную.
    """
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
    """
    Авторизация пользователя.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Страница входа или редирект на главную.
    """
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
    """
    Выход пользователя из аккаунта.

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Редирект на главную страницу.
    """
    logout(request)
    return redirect('/')


def game(request):
    """
    Отображает страницу игры "Угадай флаги".

    Args:
        request: HTTP-запрос.

    Returns:
        HttpResponse: Страница с игрой.
    """
    return render(request, 'flag_game/game.html')


def get_question(request):
    """
    API для получения случайного вопроса с тремя вариантами флагов.

    Args:
        request: HTTP-запрос.

    Returns:
        JsonResponse: JSON с вопросом и вариантами ответов.
    """
    correct_id = random.choice(list(FLAGS_DATABASE.keys()))
    correct_country = get_country_by_id(correct_id)

    other_ids = get_random_flags(exclude_id=correct_id)

    option_ids = [correct_id] + other_ids
    random.shuffle(option_ids)

    options = []
    for flag_id in option_ids:
        options.append({
            'id': flag_id,
            'image_url': f'/static/flags/{FLAGS_DATABASE[flag_id]["file"]}'
        })

    return JsonResponse({
        'question': f'Какой флаг принадлежит стране "{correct_country}"?',
        'correct_id': correct_id,
        'options': options
    })


def check_answer(request):
    """
    API для проверки ответа пользователя.

    Args:
        request: HTTP-запрос с JSON-телом {selected_id, correct_id}.

    Returns:
        JsonResponse: JSON с результатом проверки и сообщением.
    """
    data = json.loads(request.body)
    selected_id = data.get('selected_id')
    correct_id = data.get('correct_id')

    is_correct = (selected_id == correct_id)
    correct_country = get_country_by_id(correct_id)

    return JsonResponse({
        'correct': is_correct,
        'message': 'Верно! 🎉' if is_correct
        else f'Неверно! 😢 Правильный флаг - {correct_country}'
    })