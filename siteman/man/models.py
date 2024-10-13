from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.urls import reverse


# from django.utils.text import slugify


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Man.Status.PUBLISHED)


class PublishedManagerRelated(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(posts__is_published=Man.Status.PUBLISHED)


class Man(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        default=None, blank=True,
        null=True,
        verbose_name='Фото',
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='Slug',
        validators=[
            MinLengthValidator(5, message="Минимум 5 символов"),
            MaxLengthValidator(100),
        ]
    )
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
        verbose_name='Опубликовано',
    )
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='posts', verbose_name='Теги')
    wife = models.OneToOneField(
        'Wife',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='mun',
        verbose_name='Супруга',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='posts', null=True,
        default=None,
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Известный мужик'
        verbose_name_plural = 'Известные мужики'
        ordering = ['-time_create']

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()
    published = PublishedManagerRelated()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = models.Manager()
    published = PublishedManagerRelated()

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Wife(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    w_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')
