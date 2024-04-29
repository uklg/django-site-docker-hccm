# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse
from django.utils import timezone

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def lastmod(self,item):
        return timezone.now()

    def items(self):
        return ['demolition',]

    def location(self, item):
        return reverse(item)

