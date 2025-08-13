# starships/views.py
import logging
from rest_framework import generics
from rest_framework.exceptions import NotFound
from django.db.models import Q

from .models import Starship
from .serializers import StarshipSerializer

logger = logging.getLogger(__name__)


# --- Listar con paginación y búsqueda ---
class StarshipListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista de naves espaciales (paginada).
    Filtro opcional por parámetro ?q= para buscar en nombre.
    POST: Crear nueva nave.
    """
    serializer_class = StarshipSerializer

    def get_queryset(self):
        queryset = Starship.objects.all().order_by("id")
        query = self.request.query_params.get("q")
        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        return queryset


# --- Recuperar, actualizar, eliminar ---
class StarshipRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Recuperar nave por ID (log si ID negativo).
    PUT/PATCH: Modificar nave.
    DELETE: Eliminar nave.
    """
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer

    def get_object(self):
        obj = super().get_object()
        if not obj:
            raise NotFound("Nave no encontrada.")
        return obj
