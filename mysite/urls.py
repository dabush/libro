"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from authors.sitemaps import AuthorSiteMap, BookSiteMap
from .routers import router

sitemaps = {
    'authors': AuthorSiteMap,
    'books': BookSiteMap,
}

urlpatterns = [
    path('', include('home.urls')),
    path('', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),
    path('authors/', include('authors.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('api/', include(router.urls)),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)