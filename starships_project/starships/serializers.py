""" serializers.py """
from rest_framework import serializers

from .models import Starship


class StarshipSerializer(serializers.ModelSerializer):
    """ Starship Serializer """
    class Meta:
        """ Meta """
        model = Starship
        fields = '__all__'
