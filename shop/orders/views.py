from django.db import transaction

from rest_framework import viewsets, response, status
from rest_framework.decorators import action

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @transaction.atomic
    @action(
        detail=False,
        methods=['post'],
        url_path='create',
    )
    def create_order(self, request):
        cart = request.user.cart
        order = Order.objects.create(user=request.user)
        order.items.set(cart.items.all())

        cart.items.clear()

        serializer = self.get_serializer(order)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
