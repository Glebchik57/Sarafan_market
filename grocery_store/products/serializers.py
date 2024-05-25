from rest_framework import serializers
from django.db.models import Sum

from .models import Products, Basket, ProductsToBasket


class ProductsSerializer(serializers.ModelSerializer):
    full_category = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ('id', 'name', 'slug', 'price', 'image', 'full_category',)

    def get_full_category(self, obj):
        sub_cat = obj.sub_cat
        category = sub_cat.category
        return f'{category.name}/{sub_cat.name}'


class BasketSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('user', 'products', 'cost')

    def get_cost(self, obj):
        products = Basket.products_to_basket.filter(basket=obj)
        cost = products.aggregate(Sum('price'))
        return cost


class ProductToBasketSerializer(serializers.ModelSerializer):
    products = ProductsSerializer()
    basket = BasketSerializer()

    class Meta:
        model = ProductsToBasket
        fields = ('basket', 'product', 'amount')
