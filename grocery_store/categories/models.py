from django.db import models


class Categories(models.Model):
    '''Модель для хранения объектов категорий'''
    name = models.CharField(max_length=256, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        verbose_name='Изображение подкатегории',
        upload_to="static/categories",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    '''Модель для хранения объектов подкатегорий'''
    category = models.ForeignKey(
        Categories,
        verbose_name='Категория',
        related_name='subcategories',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=256,
        verbose_name='Название подкатегории'
    )
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        verbose_name='Изображение подкатегории',
        upload_to="static/subcategories",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name
