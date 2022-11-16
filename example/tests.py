from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class ProductosAPITest(TestCase):
    """API para testear los servicios de productos"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_listar_productos(self):
        url = reverse("productos")
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, status.HTTP_200_OK)
