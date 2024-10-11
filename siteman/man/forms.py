from django import forms
from .models import Category, Wife


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        required=False, label='Контент'
    )
    is_published = forms.BooleanField(required=False, initial=True, label='Статус')
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Категория не выбрана',
        label='Категория'
    )
    wife = forms.ModelChoiceField(
        queryset=Wife.objects.all(),
        required=False,
        empty_label='Не женат',
        label='Супруга'
    )
