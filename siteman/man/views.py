from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddPostForm, UploadFileForm
from .models import Man, Category, TagPost, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить страницу', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'log_in'}
]


# def index(request):
#     posts = Man.published.all().select_related('cat')
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': 0
#     }
#     return render(request, 'man/index.html', context=data)


class ManHome(ListView):
    # model = Man
    template_name = 'man/index.html'
    context_object_name = 'posts'

    extra_context = {
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0
    }

    def get_queryset(self):
        return Man.published.all().select_related('cat')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная страница'
    #     context['menu'] = menu
    #     context['posts'] = Man.published.all().select_related('cat')
    #     context['cat_selected'] = int(self.request.GET.get('cat_id', 0))
    #     return context


# def handle_uploaded_file(f):


#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request: WSGIRequest):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()

    data = {
        'title': 'О нашем сайте',
        'menu': menu,
        'form': form,
    }
    return render(request, template_name='man/about.html', context=data)


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


# def show_post(request, post_slug):
#     post = get_object_or_404(Man, slug=post_slug)
#     data = {
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': None,
#     }
#     return render(request, template_name='man/post.html', context=data)


class ShowPost(DetailView):
    model = Man
    template_name = 'man/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        context['title'] = f'Статья: {post.title}'
        context['menu'] = menu
        context['cat_selected'] = None
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Man.published, slug=self.kwargs[self.slug_url_kwarg])


# def add_page(request: WSGIRequest):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             #     Man.objects.create(**form.cleaned_data)
#             #     uri = reverse('home')
#             #     return redirect(uri)
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#             form.save()
#             uri = reverse('home')
#             return redirect(uri)
#     else:
#         form = AddPostForm()
#
#     data = {
#         'title': "Добавление статьи",
#         'menu': menu,
#         'form': form
#     }
#     return render(request, template_name='man/add_page.html', context=data)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'man/add_page.html'
    # success_url = reverse_lazy('home')

    extra_context = {
        'title': "Добавление статьи",
        'menu': menu,
    }


class UpdatePage(UpdateView):
    model = Man
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'man/add_page.html'
    success_url = reverse_lazy('home')

    extra_context = {
        'title': "Редактирование статьи",
        'menu': menu,
    }


# class AddPage(View):
#     def get(self, request: WSGIRequest):
#         form = AddPostForm()
#         data = {
#             'title': "Добавление статьи",
#             'menu': menu,
#             'form': form
#         }
#         return render(request, template_name='man/add_page.html', context=data)
#
#     def post(self, request: WSGIRequest):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             uri = reverse('home')
#             return redirect(uri)
#         data = {
#             'title': "Добавление статьи",
#             'menu': menu,
#             'form': form
#         }
#         return render(request, template_name='man/add_page.html', context=data)


def contact(request):
    return HttpResponse('Вот здесь с нами можно связаться - 8 (800)-555-35-35')


def log_in(request):
    return HttpResponse('БД пока нету, терпите')


# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Man.published.filter(cat=category).select_related('cat')
#     data = {'title': f'Рубрика: {category.name}',
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': category.pk,
#             }
#
#     return render(request, 'man/index.html', context=data)


class ManCategory(ListView):
    template_name = 'man/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Man.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        context['title'] = f'Категория - {cat.name}'
        context['menu'] = menu
        context['cat_selected'] = cat.pk
        return context


# def show_tag_post_list(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = Man.published.filter(tags=tag)
#
#     data = {
#         'title': f'Тeг: {tag.tag}',
#         'menu': menu,
#         'posts': posts,
#         'cat_selected': None,
#     }
#
#     return render(request, 'man/index.html', data)


class ManTag(ListView):
    template_name = 'man/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Man.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.get(slug=self.kwargs['tag_slug'])
        context['title'] = f'Тег - {tag.tag}'
        context['menu'] = menu
        context['cat_selected'] = None
        return context
