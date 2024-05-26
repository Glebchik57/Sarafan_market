from django.contrib import admin
from .models import Categories, SubCategories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image',)
    search_fields = ('name',)
    list_filter = ('id',)


class SubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'image',)
    search_fields = ('name',)
    list_filter = ('id',)


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(SubCategories, SubCategoriesAdmin)
