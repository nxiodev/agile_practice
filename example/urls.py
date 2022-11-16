from django.urls import path
from .views import ProductsViewSet

listar_productos = {"get": "listar_productos"}

urlpatterns = [
    path("productos/", ProductsViewSet.as_view({**listar_productos}), name="productos"),
]
