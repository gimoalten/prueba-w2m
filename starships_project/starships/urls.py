# starships/urls.py
from django.urls import path
from .views import StarshipListCreateView, StarshipRetrieveUpdateDestroyView

urlpatterns = [
    path('', StarshipListCreateView.as_view(), name='starship-list'),
    path('<int:pk>/', StarshipRetrieveUpdateDestroyView.as_view(), name='starship-detail'),
]
