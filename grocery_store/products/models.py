from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

from categories.models import SubCategories


User = get_user_model()


class Products(models.Model):
    '''Модель для хранения объектов товаров'''
    name = name = models.CharField(
        max_length=256,
        verbose_name='Название продукта'
    )
    slug = models.SlugField(unique=True)
    price = models.FloatField(verbose_name='Цена продукта')
    image_large = models.ImageField(upload_to='product_images/large/', blank=True, null=True)
    image_medium = models.ImageField(upload_to='product_images/medium/', blank=True, null=True)
    image_small = models.ImageField(upload_to='product_images/small/', blank=True, null=True)
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
    '''Модель для хранения объектов корзин пользователей'''
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        related_name='busket',
        on_delete=models.CASCADE
    )
    products = models.ManyToManyField(
        Products,
        through='ProductsToBasket',
        verbose_name='Продукты',
        related_name='busket',
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины пользователей'


class ProductsToBasket(models.Model):
    '''Модель для связи товаров и корзин пользователей'''
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name='продукт',
        related_name='products_to_basket'
    )
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        verbose_name='корзина',
        related_name='products_to_basket'
    )
    amount = models.IntegerField(
        verbose_name='количество продукта',
        default=1,
        validators=[MinValueValidator(1, 'Минимальное добавляемое количество - 1')],
    )

    class Meta:
        verbose_name = 'Продукт для корзины'
