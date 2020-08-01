from django.urls import path
from .views import CursoListView, CursoDetailView

urlpatterns = [
    path('', CursoListView.as_view(), name='eventos'),
    path('evento/<int:pk>', CursoDetailView.as_view(), name='evento')
]