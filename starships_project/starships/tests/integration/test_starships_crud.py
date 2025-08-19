""" integration/test_starships_crud.py """
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from starships.models import Starship


class StarshipAPITestCase(TestCase):
    """ Starship API TestCase"""
    def setUp(self):
        self.client = APIClient()
        self.starship1 = Starship.objects.create(name="X-Wing", model="T-65B")
        self.starship2 = Starship.objects.create(name="Millennium Falcon", model="YT-1300f")

    def test_list_starships(self):
        """ test list starships """
        response = self.client.get("/api/starships/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.json())

    def test_search_starships(self):
        """ test search starships """
        response = self.client.get("/api/starships/?q=wing")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json()["results"]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "X-Wing")

    def test_retrieve_starship(self):
        """ test retrieve starship """
        response = self.client.get(f"/api/starships/{self.starship1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["name"], "X-Wing")

    def test_create_starship(self):
        """ test create starship """
        data = {"name": "TIE Fighter", "model": "Twin Ion Engine"}
        response = self.client.post("/api/starships/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Starship.objects.count(), 3)

    def test_update_starship(self):
        """ test update starship """
        data = {"name": "Updated X-Wing"}
        response = self.client.patch(f"/api/starships/{self.starship1.id}/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.starship1.refresh_from_db()
        self.assertEqual(self.starship1.name, "Updated X-Wing")

    def test_delete_starship(self):
        """ test delete starship """
        response = self.client.delete(f"/api/starships/{self.starship1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Starship.objects.count(), 1)

    def test_negative_id_logs(self):
        """ test negative id logs """
        response = self.client.get("/api/starships/-1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
