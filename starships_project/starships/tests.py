# starships/tests.py
from django.test import TestCase
from .models import Starship

class StarshipModelTest(TestCase):
    def test_create_starship(self):
        ship = Starship.objects.create(name="X-Wing", model="T-65B", crew=1, passengers=0)
        self.assertEqual(ship.name, "X-Wing")
        self.assertEqual(Starship.objects.count(), 1)
