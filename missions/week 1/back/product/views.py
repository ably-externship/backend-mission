from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.views.generic.edit import FormMixin

from comment.forms import CommentCreationForm
from product.forms import ProductCreationForm
from product.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'product/create.html'

    def get_success_url(self):
        return reverse('product:detail', kwargs={'pk': self.object.pk})


class ProductDetailView(DetailView, FormMixin):
    model = Product
    form_class = CommentCreationForm
    context_object_name = 'target_product'
    template_name = 'product/detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'target_product'
    success_url = reverse_lazy('product:list')
    template_name = 'product/delete.html'


PRODUCT_PAGE_SIZE = 2


def product_list_view(request):
    # 1. 파라미터를 받는다. name, page
    search_value = request.GET.get('search')

    search_filter = Q()
    if search_value:
        search_filter |= Q(name__contains=search_value)
        search_filter |= Q(description__contains=search_value)

    products = Product.objects.filter(search_filter)

    page = request.GET.get('page')

    # 3. 결과 쿼리셋에 대한 페이지네이터 객체를 만든다
    paginator = Paginator(products, PRODUCT_PAGE_SIZE)

    # 4. 페이지네이터를 통해 페이징 처리 된 페이지 객체를 구한다
    page_obj = paginator.get_page(page)

    # 5. 템플릿을 통해 렌더링 한다. 필요한 파라미터들은 context 에 싣어서 함께 전달한다
    return render(
        request,
        'product/list.html',
        context={
            'paginator': paginator,
            'page_obj': page_obj,
            'product_list': page_obj.object_list,
        }
    )


class ProductListview(ListView):
    context_object_name = 'product_list'
    template_name = 'product/list.html'
    paginate_by = 2

    def get_queryset(self):
        return Product.objects.all()
