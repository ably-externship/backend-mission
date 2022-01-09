from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Question
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView

from .forms import SearchForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    # return HttpResponse("ABLY")
    page = request.GET.get('page', '1')

    products = Product.objects.all().order_by('-created_at')

    paginator = Paginator(products, 4)
    result = paginator.get_page(page)

    context = {
        'form': SearchForm,
        'products': result,
    }
    return render(request, 'goods/index.html', context)


class FormWithSearchView(FormView):
    template_name = 'goods/index.html'
    form_class = SearchForm

    def form_valid(self, form):
        keyword = form.cleaned_data['keyword']
        products = Product.objects.filter(name__icontains=keyword).order_by('-created_at')

        context = {
            'form': form,
            'keyword': keyword,
            'products': products,
        }

        return render(self.request, self.template_name, context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'goods/detail.html', context)


@login_required
def question_create(request, product_id):
    user = request.user
    content = request.POST['content']
    question = Question(user=user, product_id=product_id, content=content)
    question.save()
    return redirect('goods:detail', product_id=product_id)
