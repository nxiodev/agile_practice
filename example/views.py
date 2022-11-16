from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from drf_yasg.utils import swagger_auto_schema
from .serializers import ProductSerializer, NotFoundSerializer


class ProductsViewSet(viewsets.GenericViewSet):
    serializer_class = Serializer

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: ProductSerializer(
                many=True
            ),
            status.HTTP_404_NOT_FOUND: NotFoundSerializer,
        },
    )
    def listar_productos(self, requests) -> Response:

        data = {
            "count": 1,
            "next": "http://next.page",
            "previous": None,
            "results":
                [
                    {
                        "name": "string",
                        "sku": "string",
                        "type": "string",
                        "cost": 0.99,
                        "price": 2.99,
                        "active": True
                    },
                    {
                        "name": "string",
                        "sku": "string",
                        "type": "string",
                        "cost": 0.99,
                        "price": 2.99,
                        "active": True
                    },
                    {
                        "name": "string",
                        "sku": "string",
                        "type": "string",
                        "cost": 0.99,
                        "price": 2.99,
                        "active": True
                    }
                ]
        }
        return Response(data=data, status=status.HTTP_200_OK)
