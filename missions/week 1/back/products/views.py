from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Product
from .forms import SearchForm, QuestionForm


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


def question(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            if request.user.is_anonymous:
                return redirect(reverse('users:login'))
            question.user = request.user
            question.product = product
            question.save()
            return redirect(question)
    else:
        form = QuestionForm()
    return render(request, 'products/question.html', {'form': form, 'product': product})
