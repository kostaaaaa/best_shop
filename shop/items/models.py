from django.db import models

from utils.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    founded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Product(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='products')
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f'Product: {self.name}'


class Item(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'Product: {self.product.name}. Price: {self.price}'
