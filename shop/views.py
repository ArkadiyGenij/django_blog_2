from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from shop.forms import ProductForm, VersionForm, ModeratorProductForm
from .models import Product, Version, Category


# Create your views here.

class ContactView(TemplateView):
    template_name = 'shop/contact.html'


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.prefetch_related('versions').filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_moderator'] = self.request.user.groups.filter(name='Модераторы').exists()
        return context


@method_decorator(cache_page(60 * 10), name='dispatch')
class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('shop:product_list')


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')

    def get_form_class(self):
        if self.request.user.groups.filter(name='Модераторы').exists():
            return ModeratorProductForm
        return ProductForm

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.groups.filter(name='Модераторы').exists()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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


class CategoryListView(ListView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('shop:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('shop:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('shop:category_list')
