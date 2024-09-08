from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from shop.forms import ProductForm, VersionForm
from .models import Product, Version


# Create your views here.


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.prefetch_related('versions').all()


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shop:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')


class ContactView(TemplateView):
    template_name = 'shop/contact.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')


class VersionListView(ListView):
    model = Version

    def get_queryset(self, **kwargs):
        product_id = self.kwargs['pk']
        return Version.objects.filter(product_id=product_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['pk']
        context['product'] = Product.objects.get(pk=product_id)
        return context


class VersionCreateView(CreateView):
    model = Version

    form_class = VersionForm

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shop:version_list', kwargs={'pk': self.object.product.id})


class VersionUpdateView(UpdateView):
    model = Version

    form_class = VersionForm

    def get_success_url(self):
        return reverse('shop:version_list', kwargs={'pk': self.object.product.id})


class VersionDeleteView(DeleteView):
    model = Version

    def get_success_url(self):
        return reverse('shop:version_list', kwargs={'pk': self.object.product.id})
