from django.shortcuts import render
from .models import Tutorial
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class TutorialListView(ListView):
    model = Tutorial
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'tutoriales'
        return context

class TutorialDetailView(DetailView):
    model = Tutorial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = 'tutoriales'
        return context
