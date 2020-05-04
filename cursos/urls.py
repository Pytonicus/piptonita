from django.urls import path
from .views import CursoListView, CursoDetailView

urlpatterns = [
    path('', CursoListView.as_view(), name='cursos'),
    path('curso/<int:pk>', CursoDetailView.as_view(), name='curso')
]