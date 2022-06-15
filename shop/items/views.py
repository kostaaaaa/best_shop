from django.db import transaction
from rest_framework import viewsets, response, status
from rest_framework.decorators import action

from .models import Brand, Item, Product
from .serializers import BrandSerializer, ProductSerializer, ItemSerializer
from orders.models import Cart


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @transaction.atomic
    @action(
        detail=True,
        methods=['post'],
        url_path='add-to-cart'
    )
    def add_item_to_cart(self, request, pk=None):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        item = self.get_object()
        cart.items.add(item)
        return response.Response(status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['get'],
        url_path='cart',
    )
    def cart(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        serializer = ItemSerializer(cart.items.all(), many=True)
        return response.Response(serializer.data)
