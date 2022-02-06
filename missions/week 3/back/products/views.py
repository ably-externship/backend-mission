from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import Q
from django.views import View

from project.settings import LOGIN_URL

from .forms import InquiryForm
from .forms import ProductSearchForm
from inquirys.models import Inquiry
from .models import Product
from vendors.models import Vendor
from users.models import User

from .permissions import IsVendorOrReadOnly, IsStaffOrReadOnly
from .serializers import ProductSerializer
from .serializers import VendorSerializer

from rest_framework import generics, permissions

from braces.views import CsrfExemptMixin


class IndexView(generic.ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        """Return products ordered by price."""
        return Product.objects.order_by('name')


class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inquirys'] = Inquiry.objects.filter(
            product_id=self.kwargs['pk'])
        context['inquiry_form'] = InquiryForm()
        return context


class SearchFormView(FormView):
    form_class = ProductSearchForm
    template_name = 'product/product_search.html'

    def form_valid(self, form):
        search_term = form.cleaned_data['search_term']
        product_list = Product.objects.filter(
            Q(name__icontains=search_term) |
            Q(description__icontains=search_term)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = search_term
        context['object_list'] = product_list

        return render(self.request, self.template_name, context)


def search(request):
    products = Product.objects.all().order_by('-id')

    query = request.GET.get('q', "")

    if query:
        products = products.filter(name__icontains=query)
        return render(request, 'product/search.html', {'products': products, 'q': query})

    else:
        return render(request, 'product/search.html')


@login_required(login_url=LOGIN_URL)
def create_comment(request, product_id):
    comment_write = InquiryForm(request.POST)
    if comment_write.is_valid():
        comments = comment_write.save(commit=False)
        comments.product = get_object_or_404(Product, pk=product_id)
        comments.user = request.user
        comments.save()
    return redirect('product:detail', product_id)


class ProductList(CsrfExemptMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


<< << << < HEAD: missions/week 3/back/products/views.py
# [permissions.IsAuthenticatedOrReadOnly]
permission_classes = [permissions.IsAuthenticated]
== == == =
permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsStaffOrReadOnly, ]
>>>>>> > 6bf6ff228541bf7e5a5f9c94ccf86e8263ff5c3c: missions/week 3/back/product/views.py


class ProductDetail(CsrfExemptMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly, ]


class VendorProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsVendorOrReadOnly]

    def get_queryset(self):
        vendor = Vendor.objects.get(user=self.request.user)
        queryset = Product.objects.filter(vendor=vendor)
        return queryset


class VendorProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsVendorOrReadOnly]

    def get_queryset(self):
        vendor = Vendor.objects.get(user=self.request.user)
        product = Product.objects.filter(
            pk=self.kwargs.get('pk'), vendor=vendor)

        return product


class VendorList(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetail(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
