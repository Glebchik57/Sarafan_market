from rest_framework import serializers
from django.db.models import Sum, F
from drf_extra_fields.fields import Base64ImageField

from .models import Products, Basket, ProductsToBasket


class ProductsSerializer(serializers.ModelSerializer):
    full_category = serializers.SerializerMethodField()
    image_large = Base64ImageField()
    image_medium = Base64ImageField()
    image_small = Base64ImageField()

    class Meta:
        model = Products
        fields = (
            'id',
            'name',
            'slug',
            'price',
            'image_large',
            'image_medium',
            'image_small',
            'full_category',
        )

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
        products_to_basket = obj.products_to_basket.all()
        cost = products_to_basket.aggregate(
            total_cost=Sum(F('product__price') * F('amount'))
        )
        return cost.get('total_cost', 0)


class ProductToBasketSerializer(serializers.ModelSerializer):
    products = ProductsSerializer()
    basket = BasketSerializer()

    class Meta:
        model = ProductsToBasket
        fields = ('basket', 'product', 'amount')
