from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.core.paginator import Paginator
from django.views import generic
from django.db.models import Q
from django.views import View

from project.settings import LOGIN_URL

from product.forms import InquiryForm
from product.forms import ProductSearchForm
from inquiry.models import Inquiry
from product.models import Product
from vendor.models import Vendor
from user.models import User

from product.permissions import IsVendorOrReadOnly, IsStaffOrReadOnly
from product.serializers import ProductSerializer
from product.serializers import VendorSerializer
from product.serializers import UserSerializer

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
        kw = form.cleaned_data['kw']
        product_list = Product.objects.filter(Q(name__icontains=kw) | Q(
            description__icontains=kw)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = kw
        context['object_list'] = product_list

        return render(self.request, self.template_name, context)

def search(request):
    products = Product.objects.all().order_by('-id')

    q = request.GET.get('q', "")

    if q:
        products = products.filter(name__icontains=q)
        print(products)
        return render(request, 'product/search.html', {'products': products, 'q': q})

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsStaffOrReadOnly, ]


class ProductDetail(CsrfExemptMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, 
                          IsStaffOrReadOnly, ]


class VendorList(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorDetail(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer



