from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
# 페이징을 사용하기 위해 추가
from django.core.paginator import Paginator

# 검색기능 query filter를 사용하기 위해 추가
from django.db.models import Q

from .models import Product, Category, Brand, Image, Comment, Cart


# Create your views here.
# home
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context


# Product list
class ProductListView(ListView):
    template_name = 'product/product_list.html'
    model = Product
    ordering = 'pk'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)

        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context


# category product
class CategoryView(ProductListView):
    paginate_by = 4
    ordering = 'pk'

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)
        product_list = Product.objects.filter(category=category)

        return product_list


# brand product
class BrandView(ProductListView):
    paginate_by = 4
    ordering = 'pk'

    def get_queryset(self):
        slug = self.kwargs['slug']
        brand = Brand.objects.get(slug=slug)
        product_list = Product.objects.filter(brand=brand)

        return product_list


# Product detail
class ProductDetailView(DetailView):
    template_name = 'product/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)

        # 상품 상세 페이지의 이미지
        context['images'] = Image.objects.filter(product_id=self.kwargs['pk'])
        # 질문 리스트
        context['comments'] = Comment.objects.filter(product_id=self.kwargs['pk'])

        return context


# Search
class SearchView(ProductListView):
    paginate_by = 4

    def get_queryset(self):
        q = self.kwargs['q']
        product_list = Product.objects.filter(
            Q(name__contains=q) | Q(brand__name__contains=q)
        ).distinct()

        return product_list

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)

        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context


# Cart
class CartView(TemplateView):
    template_name = 'product/cart.html'
    ordering = '-created_at'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)

        user_id = self.request.user.id
        cart = Cart.objects.filter(user_id=user_id)
        total_price = 0

        for cart in cart:
            total_price += cart.product.price * cart.quantity

        if cart is not None:
            context['total'] = total_price

        context['carts'] = Cart.objects.filter(user__id=user_id)

        return context


