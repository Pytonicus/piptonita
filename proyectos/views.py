from django.shortcuts import render
from .models import Categoria, Proyecto, Capitulo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ProyectoListView(ListView):
    model = Proyecto
    paginated_by = 10

    def get_queryset(self):
        qs = super().get_queryset()

        try:
            query = qs.filter(categoria = self.kwargs['pk'])
        except:
            query = qs

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'proyectos'
        context["tecnologias"] = Categoria.objects.all()
        context['proyectos'] = self.get_queryset()
        
        return context

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyectos/proyecto_detail.html'

    def get_queryset(self):
        qs = super().get_queryset()

        try:
            query = Capitulo.objects.filter(pk = self.kwargs['pk'])
        except:
            query = qs

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'proyectos'
        context['capitulos'] = Capitulo.objects.filter(proyecto = self.kwargs['pk'])
        try: 
            context['paso'] = context['capitulos'][0]

        except:
            context['paso'] = ""

        return context

class CapituloDetailView(DetailView):
    model = Capitulo
    template_name = 'proyectos/proyecto_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'proyectos'
        context['capitulos'] = Capitulo.objects.all()
        context['paso'] = context['capitulo']
        print(context['paso'])

        return context
    