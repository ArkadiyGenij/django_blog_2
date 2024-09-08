# Generated by Django 5.0.7 on 2024-09-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_unpublish_product', 'Can unpublish product'), ('can_change_category', 'Can change product category'), ('can_change_product', 'Can change product description')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
