from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from man.views import page_not_found

from debug_toolbar.toolbar import debug_toolbar_urls

from siteman import settings

from django.contrib.sitemaps.views import sitemap

from django.views.decorators.cache import cache_page
from man.sitemaps import PostSiteMap, CategorySiteMap, TagSiteMap

sitemaps = {
    'posts': PostSiteMap,
    'categories': CategorySiteMap,
    'tags': TagSiteMap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('man.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('captcha/', include('captcha.urls')),

    path('sitemap.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()

handler404 = page_not_found

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Известные мужики'
