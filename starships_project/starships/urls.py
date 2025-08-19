""" urls.py """
from django.urls import path

from .views import StarshipDetailView, StarshipListCreateView

urlpatterns = [
    path('', StarshipListCreateView.as_view(), name='starship-list'),
    path('<slug:pk>/', StarshipDetailView.as_view(), name='starship-detail'),
]
