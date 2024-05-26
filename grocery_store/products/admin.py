from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'price',
        'image_large',
        'image_medium',
        'image_small',
        'sub_cat',
    )
    search_fields = ('name',)


admin.site.register(Products, ProductsAdmin)
