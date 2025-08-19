""" apps.py """
from django.apps import AppConfig


class StarshipsConfig(AppConfig):
    """ Starship Config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'starships'
