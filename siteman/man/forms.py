from captcha.fields import CaptchaField
from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Wife, Man


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


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'cols': 60,
            'rows': 10,
        }))
    captcha = CaptchaField()