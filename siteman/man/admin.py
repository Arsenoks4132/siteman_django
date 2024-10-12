from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Man, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус мужчин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Женат'),
            ('single', 'Не женат')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(wife__isnull=False)
        return queryset


@admin.register(Man)
class ManAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'post_photo', 'wife', 'tags')  # Поля для редактирования
    # exclude = ('tags', 'is_published')  # Исключаемые из редактирования поля
    readonly_fields = ('post_photo', )
    prepopulated_fields = {'slug': ('title', )}
    filter_horizontal = ('tags', )
    list_display = ('id', 'title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ('time_create',)
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ('set_published', 'set_draft')
    search_fields = ('title__startswith', 'cat__name')
    list_filter = (MarriedFilter, 'cat__name', 'is_published')
    save_on_top = True

    @admin.display(description='Фотография', ordering='content')
    def post_photo(self, man: Man):
        if man.photo:
            return mark_safe(f'<img src={man.photo.url} width=50>')
        return 'Без фото'

    @admin.action(description='Сделать опубликованными')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Man.Status.PUBLISHED)
        self.message_user(request, f'Опубликовано {count} записей')

    @admin.action(description='Сделать черновиками')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Man.Status.DRAFT)
        self.message_user(request, f'Снято с публикации {count} записей', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
