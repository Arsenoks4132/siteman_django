from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.MonthNumberConverter, 'month2')

urlpatterns = [
    path('', views.ManHome.as_view(), name='home'),
    path('about/', views.about, name='about'),

    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_slug'),
    path('month/<month2:mn>/', views.month, name='month'),

    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive, name="re_archive"),

    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),

    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('log_in/', views.log_in, name='log_in'),
    path('category/<slug:cat_slug>/', views.ManCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.ManTag.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
]
