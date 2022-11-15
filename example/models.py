from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    volume = models.FloatField()
    weight = models.FloatField()
    price = models.FloatField()
    cost = models.FloatField()
    active = models.BooleanField(default=True)


class Customer(models.Model):
    name = models.CharField(max_length=50)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    date = models.DateField()


class Shipments(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField()
