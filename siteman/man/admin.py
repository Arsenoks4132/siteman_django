from django.contrib import admin, messages
from .models import Man, Category


@admin.register(Man)
class ManAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ('time_create',)
    list_editable = ('is_published',)
    list_per_page = 10
    actions = ('set_published', 'set_draft')

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, man: Man):
        return f'Описание {len(man.content)} символов'

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
