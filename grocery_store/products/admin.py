from django.contrib import admin

from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'image', 'sub_cat')
    search_fields = ('name',)


admin.site.register(Products, ProductsAdmin)
