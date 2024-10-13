from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .models import Category, Wife, Man


# class RussianValidator:
#     ALLOWED_CHARS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789- '
#     code = 'Russian'
#
#     def __init__(self, message=None):
#         self.message = message if message else 'Должны присутствовать только русские символы, цифры, дефис и пробел.'
#
#     def __call__(self, value, *args, **kwargs):
#         if not (set(value) <= set(self.ALLOWED_CHARS)):
#             raise ValidationError(self.message, code=self.code)

class AddPostForm(forms.ModelForm):
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

    class Meta:
        model = Man
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat', 'wife', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {
            'slug': 'URL',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина не должна превышать 50 символов")

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Файл")