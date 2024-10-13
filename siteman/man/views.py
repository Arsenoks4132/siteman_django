from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddPostForm, UploadFileForm
from .models import Man, Category, TagPost, UploadFiles
from .utils import DataMixin


class ManHome(DataMixin, ListView):
    template_name = 'man/index.html'
    context_object_name = 'posts'

    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Man.published.all().select_related('cat')


def about(request: WSGIRequest):
    contact_list = Man.published.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    data = {
        'title': 'О нашем сайте',
        'page_obj': page_obj,
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


class ShowPost(DataMixin, DetailView):
    model = Man
    template_name = 'man/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Man.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    title_page = 'Добавление статьи'
    template_name = 'man/add_page.html'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(DataMixin, UpdateView):
    model = Man
    fields = ['title', 'content', 'photo', 'is_published', 'cat']
    template_name = 'man/add_page.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование статьи'


def contact(request):
    return HttpResponse('Вот здесь с нами можно связаться - 8 (800)-555-35-35')


def log_in(request):
    return HttpResponse('БД пока нету, терпите')


class ManCategory(DataMixin, ListView):
    template_name = 'man/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Man.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat

        return self.get_mixin_context(
            context,
            title=f'Категория - {cat.name}',
            cat_selected=cat.pk,
        )


class ManTag(DataMixin, ListView):
    template_name = 'man/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Man.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['posts'][0].tags.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(
            context,
            title=f'Тег - {tag.tag}'
        )
