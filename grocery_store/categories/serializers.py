from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from .models import Categories, SubCategories


class SubCategoriesSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели SubCategories'''
    image = Base64ImageField()

    class Meta:
        model = SubCategories
        fields = ('name', 'slug', 'category', 'image')


class CategoriesSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели Categories'''
    sub_cat = serializers.SerializerMethodField()
    image = Base64ImageField()

    class Meta:
        model = Categories
        fields = ('name', 'slug', 'image', 'sub_cat')

    def get_sub_cat(self, obj):
        '''Метод для получения подкатегорий текущей категории'''
        sub_cat = obj.subcategories.all()
        serializer = SubCategoriesSerializer(sub_cat, many=True)
        return serializer.data
