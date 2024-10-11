from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404

from .forms import AddPostForm
from .models import Man, Category, TagPost

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить страницу', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'log_in'}
]


def index(request):
    posts = Man.published.all().select_related('cat')
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts,
            'cat_selected': 0}
    return render(request, 'man/index.html', context=data)


def about(request):
    data = {
        'title': 'О нашем сайте',
        'menu': menu,
        'text': 'Что-то о нашем чудесном сайте'

    }
    return render(request, 'man/about.html', data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статья категорий</h1><p>page id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статья категорий</h1><p>slug: {cat_slug}</p>")


def month(request, mn):
    if not (1 <= mn <= 12):
        url = reverse('cats_slug', args=(f'month_{mn}',))
        return redirect(url)
    return HttpResponse(f"<h2>Статья за месяц</h2><p>Месяц: {mn}</p>")


def archive(request, year):
    return HttpResponse(f'<h3>Архив за {year} год</h3>')


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h3>Мы пока ничего не нашли, пока!!!</h3>")


def show_post(request, post_slug):
    post = get_object_or_404(Man, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': None,
    }
    return render(request, template_name='man/post.html', context=data)


def add_page(request: WSGIRequest):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()

    data = {
        'title': "Добавление статьи",
        'menu': menu,
        'form': form
    }
    return render(request, template_name='man/add_page.html', context=data)


def contact(request):
    return HttpResponse('Вот здесь с нами можно связаться - 8 (800)-555-35-35')


def log_in(request):
    return HttpResponse('БД пока нету, терпите')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Man.published.filter(cat=category).select_related('cat')
    data = {'title': f'Рубрика: {category.name}',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk,
            }

    return render(request, 'man/index.html', context=data)


def show_tag_post_list(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = Man.published.filter(tags=tag)

    data = {
        'title': f'Тeг: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'man/index.html', data)
