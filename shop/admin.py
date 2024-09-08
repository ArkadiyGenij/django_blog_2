from django.contrib import admin

from shop.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('name', 'price', 'category')
    search_fields = ('name', 'price')


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version_name', 'version_number')
    list_filter = ('version_name', 'version_number')
    search_fields = ('version_name', 'version_number')