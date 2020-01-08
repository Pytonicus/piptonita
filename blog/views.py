from django.shortcuts import render
from .models import Entrada
from django.views.generic.list import ListView

class EntradaListView(ListView):
    model = Entrada
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'blog'
        return context
    