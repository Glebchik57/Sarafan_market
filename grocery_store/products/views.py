from rest_framework import viewsets
from rest_framework.decorators import action

from .models import Products, Basket
from .serializers import ProductsSerializer, BasketSerializer
from categories.permissions import IsAdminOrReadOnly
from .permission import IsOwner


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsOwner,)

    @action(
        ['DELETE'],
        detail=False,
        url_path='clear_basket',
    )
    def clear_basket(self, request):
        products = Basket.products_to_basket.all()
        products.delete()
