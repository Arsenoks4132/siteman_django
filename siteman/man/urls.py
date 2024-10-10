from django.urls import path, register_converter

from . import views
from . import converters

register_converter(converters.MonthNumberConverter, 'month2')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),
    path("month/<month2:mn>/", views.month, name='month'),

    path('post/<slug:post_slug>/', views.show_post, name='post'),

    path('add_page/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('log_in/', views.log_in, name='log_in'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_post_list, name='tag')
]