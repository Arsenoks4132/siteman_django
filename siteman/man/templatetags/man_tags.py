from django import template
from man.models import Category, TagPost
from django.db.models import Count
from django.db.models.functions import Length

register = template.Library()


@register.inclusion_tag('man/list_categories.html')
def show_categories(cat_selected=None):
    cats = Category.published.annotate(total=Count('posts')).filter(total__gt=0).order_by('name')
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('man/list_tags.html')
def show_all_tags():
    tags = TagPost.published.annotate(total=Count('posts'), ln=Length('tag')).filter(total__gt=0).order_by('ln')
    return {'tags': tags}


@register.inclusion_tag('form.html')
def post_form(form=None, button='Отправить'):
    return {'form': form, 'button': button}