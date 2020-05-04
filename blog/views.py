from django.shortcuts import render
from .models import Entrada
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class EntradaListView(ListView):
    model = Entrada
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'blog'
        return context

class EntradaDetailView(DetailView):
    model = Entrada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = 'blog'
        return context