# Generated by Django 3.2 on 2024-05-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='image_large',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/large/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image_medium',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/medium/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image_small',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/small/'),
        ),
    ]
