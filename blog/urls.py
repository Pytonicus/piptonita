from django.urls import path
from .views import EntradaListView

urlpatterns = [
    path('', EntradaListView.as_view(), name='blog')
]