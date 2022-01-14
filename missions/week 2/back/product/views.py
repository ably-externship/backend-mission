from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product
from django.views.generic.edit import FormView
from product.forms import ProductSearchForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views import View
from django.contrib.auth.decorators import login_required
from inquiry.models import Inquiry
from product.forms import InquiryForm
from user.models import User
from project.settings import LOGIN_URL


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
        print("NO\n")
        return render(request, 'product/search.html')


@login_required(login_url=LOGIN_URL)
def create(request, product_id):
    comment_write = InquiryForm(request.POST)
    if comment_write.is_valid():
        comments = comment_write.save(commit=False)
        comments.product = get_object_or_404(Product, pk=product_id)
        comments.user = request.user
        comments.save()
    return redirect('product:detail', product_id)
