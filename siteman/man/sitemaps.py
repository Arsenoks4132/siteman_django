from django.contrib.sitemaps import Sitemap

from man.models import Man, Category, TagPost


class PostSiteMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Man.published.all()

    def lastmod(self, obj):
        return obj.time_update


class CategorySiteMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Category.published.all()


class TagSiteMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return TagPost.published.all()