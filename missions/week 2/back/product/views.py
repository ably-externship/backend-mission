from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView
from django.views.generic.edit import FormMixin

from comment.forms import CommentCreationForm
from product.forms import ProductCreationForm, ProductPurchaseForm
from product.models import Product, ProductOption, CartItem


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['purchases_form'] = ProductPurchaseForm(self.object)
        return context


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'target_product'
    success_url = reverse_lazy('product:list')
    template_name = 'product/delete.html'


PRODUCT_PAGE_SIZE = 5


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
        'product/list_original.html',
        context={
            'paginator': paginator,
            'page_obj': page_obj,
            'product_list': page_obj.object_list,
        }
    )


def add_cart_view(request):
    product_option_id = request.POST.get('product_option')
    product_option_id = int(product_option_id)
    product_option = ProductOption.objects.get(id=product_option_id)

    try:
        cart_item = CartItem.objects.get(user=request.user, product_option=product_option)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        CartItem.objects.create(
            user=request.user,
            product_option=product_option,
            product=product_option.product,
            quantity=1
        )
    return redirect('product:cart_items')


def cart_items_view(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('id')
    return render(request, 'product/cart_items.html', context={'cart_items': cart_items})
