from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from .models import Categories, SubCategories


class SubCategoriesSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = SubCategories
        fields = ('name', 'slug', 'image')


class CategoriesSerializer(serializers.ModelSerializer):
    sub_cat = serializers.SerializerMethodField()
    image = Base64ImageField()

    class Meta:
        model = Categories
        fields = ('name', 'slug', 'image', 'sub_cat')

    def get_sub_cat(self, obj):
        sub_cat = obj.subcategories.all()
        return sub_cat
