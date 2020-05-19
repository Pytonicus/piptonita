from django.contrib import sitemaps
from django.urls import reverse
from tutoriales.models import Tutorial
from proyectos.models import Proyecto
from cursos.models import Curso

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['blog', 'tutoriales', 'cursos', 'proyectos']

    def location(self, item):
        return reverse(item)

class TutorialSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Tutorial.objects.all()

class ProyectoSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Proyecto.objects.all()

class CursoSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Curso.objects.all()