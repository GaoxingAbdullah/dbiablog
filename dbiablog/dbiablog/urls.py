from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

from .sitemaps import CategorySiteMap, PostSiteMap

from os import name
from django.contrib import admin
from django.urls import path, include


from core.views import homepage, aboutpage, featurepage, servicepage, robots_txt

sitemaps = {"category": CategorySiteMap, "post":PostSiteMap}

urlpatterns = [
    path('sitemap.xml', sitemap, {"sitemaps": sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('about', aboutpage, name='aboutpage'),
    path('feature', featurepage, name='featurepage'),
    path('', include('blog.urls')),
    path('service', servicepage, name='servicepage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
