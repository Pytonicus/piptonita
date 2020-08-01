from django.shortcuts import render
from .models import Curso
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class CursoListView(ListView):
    model = Curso
    paginated_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'laboratorio'

        return context

class CursoDetailView(DetailView):
    model = Curso