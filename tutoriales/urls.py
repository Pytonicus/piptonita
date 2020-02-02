from django.urls import path
from .views import TutorialListView, TutorialDetailView

urlpatterns = [
    path('', TutorialListView.as_view(), name='tutoriales'),
    path('tutorial/<int:pk>/', TutorialDetailView.as_view(), name='tutorial')
]