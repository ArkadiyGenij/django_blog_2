from django.views.generic import ListView, DetailView, TemplateView

from shop.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactView(TemplateView):
    template_name = 'shop/contact.html'
