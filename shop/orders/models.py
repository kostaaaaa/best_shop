from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModel


class Cart(BaseModel):
    items = models.ManyToManyField('items.Item', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}'s cart"


STATUS_CHOICES = (
    ('PENDING', 'Pending'),
    ('IN_PROGRESS', 'In progress'),
    ('DELIVERED', 'Delivered'),
)


class Order(BaseModel):
    items = models.ManyToManyField('items.Item', related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='PENDING')
