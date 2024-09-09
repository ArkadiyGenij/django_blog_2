from django.core.cache import cache

from shop.models import Category, Product


def get_categories():
    cache_key = 'category_list'
    categories = cache.get(cache_key)

    if not categories:
        categories = Category.objects.all()
        cache.set(cache_key, categories, 60 * 60)

    return categories


def get_products():
    cache_key = 'product_list'
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(is_published=True)
        cache.set(cache_key, products, 60 * 60)

    return products
