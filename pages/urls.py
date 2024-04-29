from django.urls import path, include
from .views import contactViewD
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', contactViewD,name='demolition'),

    path('__debug__/', include('debug_toolbar.urls')),

    path('sitemap.xml', 
          sitemap, {'sitemaps': sitemaps, 'template_name':'custom_sitemap.html'},
         name='django.contrib.sitemaps.views.sitemap')

]
