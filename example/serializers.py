from rest_framework import serializers


class NotFoundSerializer(serializers.Serializer):
    """Serializador destinado solo para completar el Schema en Swagger"""

    detail = serializers.CharField(help_text="Not found")


class ProductSerializer(serializers.Serializer):
    """Serializador para el modelo Product"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    sku = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    volume = serializers.FloatField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    active = serializers.BooleanField(default=True)
