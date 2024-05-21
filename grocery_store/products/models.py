from django.db import models
from django.contrib.auth import get_user_model

from categories.models import SubCategories


User = get_user_model()


class Products(models.Model):
    name = name = models.CharField(
        max_length=256,
        verbose_name='Название продукта'
    )
    slug = models.SlugField(unique=True)
    price = models.FloatField(verbose_name='Цена продукта')
    image = models.ImageField(
        verbose_name='Изображение продукта',
        upload_to="static/subcategories"
    )
    sub_cat = models.ForeignKey(
        SubCategories,
        verbose_name='Подкатегория',
        related_name='products',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        related_name='busket',
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        Products,
        verbose_name='Продукты',
        related_name='busket',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины пользователей'
