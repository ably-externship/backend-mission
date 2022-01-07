from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from product.forms import ProductCreationForm
from product.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('product:detail', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'target_product'
    template_name = 'product/detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'target_product'
    success_url = reverse_lazy('product:list')
    template_name = 'product/delete.html'