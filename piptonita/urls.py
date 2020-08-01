"""piptonita URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, TutorialSitemap, ProyectoSitemap, CursoSitemap
from core import views
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
    'tutoriales': TutorialSitemap,
    'proyectos': ProyectoSitemap,
    'cursos': CursoSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('tutoriales/', include('tutoriales.urls')),
    path('proyectos/', include('proyectos.urls')),
    path('cursos/', include('cursos.urls')),
    path('laboratorio/', include('laboratorio.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = 'Piptonita'
admin.site.site_header = 'Piptonita - El mundo del código, los videojuegos y la cultura maker'
admin.site.index_title = 'Panel de control'