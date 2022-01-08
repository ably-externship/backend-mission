from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import SearchForm


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created_at"
    template_name = 'home.html'
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product


def search(request):
    product_name = request.GET.get('name')
    if product_name:
        form = SearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            products = Product.objects.filter(name__icontains=name).order_by("-created_at")
            return render(request, 'products/search.html', {'form': form, 'products': products})
    else:
        form = SearchForm()
    return render(request, 'products/search.html', {'form': form})
