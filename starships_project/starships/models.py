""" models.py """
from django.db import models


class Starship(models.Model):
    """ Starship """
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=200, blank=True)
    crew = models.IntegerField(default=0)
    passengers = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
