from django.urls import path
from .views import ProyectoListView, ProyectoDetailView, CapituloDetailView

urlpatterns = [
    path('', ProyectoListView.as_view(), name='proyectos'),
    path('categoria/<int:pk>', ProyectoListView.as_view(), name='categoria'),
    path('proyecto/<int:pk>/', ProyectoDetailView.as_view(), name='proyecto'),
    path('proyecto/paso/<int:pk>/', CapituloDetailView.as_view(), name='paso')
]