from rest_framework import viewsets,  status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Products, Basket, ProductsToBasket
from .serializers import (
    ProductsSerializer,
    BasketSerializer,
    ProductToBasketSerializer
)
from categories.permissions import IsAdminOrReadOnly
from .permission import IsOwner


class ProductsViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с товарами'''
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BasketViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с корзинами пользователей'''
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return Basket.objects.filter(user=user)

    @action(
        ['POST'],
        detail=False,
        url_path='add_to_basket',
    )
    def add_products(self, request):
        '''Метод добавления продуктов в корзину'''
        user = request.user
        product_id = request.data.get('product_id')
        amount = request.data.get('amount', 1)

        try:
            product = Products.objects.get(id=product_id)
            basket, created = Basket.objects.get_or_create(user=user)
            basket_item, created = ProductsToBasket.objects.get_or_create(
                basket=basket,
                product=product,
                defaults={'amount': amount}
            )
            if not created:
                basket_item.amount += amount
                basket_item.save()

            serializer = ProductToBasketSerializer(basket_item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Products.DoesNotExist:
            return Response(
                {'message': 'Продукт не найден'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(
        ['DELETE'],
        detail=False,
        url_path='remove_from_basket',
    )
    def remove_product(self, request):
        '''Метод удаления продукта из корзины'''
        user = request.user
        product_id = request.data.get('product_id')

        try:
            product = Products.objects.get(id=product_id)
            basket = Basket.objects.get(user=user)
            basket_item = ProductsToBasket.objects.get(
                basket=basket,
                product=product
            )
            basket_item.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except (Products.DoesNotExist, ProductsToBasket.DoesNotExist):
            return Response(
                {'message': 'Продукт не найден'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(
        ['DELETE'],
        detail=False,
        url_path='clear_basket',
    )
    def clear_basket(self, request):
        '''Метод очистки корзины'''
        user = request.user
        basket = Basket.objects.filter(user=user).first()
        basket.products.clear()
        return Response(
            {'message': 'Корзина очищена'},
            status=status.HTTP_204_NO_CONTENT
        )
