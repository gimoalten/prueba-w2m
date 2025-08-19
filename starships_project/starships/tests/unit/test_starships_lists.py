""" unit/test_starships_list.py """
from django.http import Http404
from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from starships.models import Starship
from starships.views import StarshipDetailView, StarshipListCreateView


class StarshipListCreateViewTests(TestCase):
    """ Starship List Create Viwe Tests"""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = StarshipListCreateView()
        Starship.objects.create(name="X-Wing", model="T-65B")
        Starship.objects.create(name="Millennium Falcon", model="YT-1300f")

    def test_get_queryset_without_filter(self):
        """ test get queryset without filter """
        req = self.factory.get("/api/starships/")
        request = Request(req)
        self.view.request = request
        qs = self.view.get_queryset()
        self.assertEqual(qs.count(), 2)

    def test_get_queryset_with_filter(self):
        """ test get queryset with filter """
        req = self.factory.get("/api/starships/?q=Falcon")
        request = Request(req)  # 👈 envolver
        self.view.request = request
        qs = self.view.get_queryset()
        self.assertEqual(qs.count(), 1)
        self.assertEqual(qs.first().name, "Millennium Falcon")


class StarshipDetailViewTests(TestCase):
    """ Starship Detail View Tests"""

    def setUp(self):
        self.factory = APIRequestFactory()
        self.starship = Starship.objects.create(name="X-Wing", model="T-65B")

    def test_get_object_valid_id(self):
        """ test get object valid id """
        view = StarshipDetailView()
        req = self.factory.get(f"/api/starships/{self.starship.id}/")
        request = Request(req)
        view.request = request
        view.kwargs = {"pk": self.starship.id}
        obj = view.get_object()
        self.assertEqual(obj, self.starship)

    def test_get_object_invalid_id(self):
        """ get object invalid id """
        view = StarshipDetailView()
        req = self.factory.get("/api/starships/9999/")
        request = Request(req)
        view.request = request
        view.kwargs = {"pk": 9999}
        with self.assertRaises(Http404):
            view.get_object()

    def test_negative_id_triggers_log(self):
        """ test negative id triggers log """
        view = StarshipDetailView()
        req = self.factory.get("/api/starships/-1/")
        request = Request(req)
        view.request = request
        view.kwargs = {"pk": -1}
        with self.assertRaises(Http404):
            view.get_object()
