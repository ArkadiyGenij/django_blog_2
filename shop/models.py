from django.conf import settings
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=150, verbose_name="Описание")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products',
                                 verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products',
                              verbose_name='Владелец', default=1)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_change_category", "Can change product category"),
            ("can_change_product", "Can change product description"),
        ]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name='Продукт')
    version_number = models.CharField(max_length=50, verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    is_current = models.BooleanField(default=False, verbose_name='Текущая версия')

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        unique_together = ('product', 'version_number')

    def __str__(self):
        return f'{self.product.name} - {self.version_name} (Версия: {self.version_number})'
