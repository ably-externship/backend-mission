from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    template_name = 'home.html'
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
