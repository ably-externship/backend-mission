from django import forms
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from questions.models import Question
from .models import *


class ProductListView(generic.ListView):
    template_name = 'products/index.html'
    model = Product
    ordering = 'pk'
    paginate_by = 8
    context_object_name = 'products'


class SearchView(ProductListView):
    def get_queryset(self):
        query = self.request.GET.get('query', '')
        products = Product.objects.filter(display_name__contains=query)
        return products


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    options = ProductOption.objects.filter(product=product)
    questions = Question.objects.filter(content_type=ContentType.objects.get_for_model(product), object_id=product_id)

    class SelectOptionForm(forms.Form):
        option = forms.ModelChoiceField(label='옵션', queryset=options)
        quantity = forms.IntegerField(label='수량', min_value=1, initial=1)

    return render(request, 'products/detail.html', {
        'product': product,
        'options': options,
        'questions': questions,
        'form': SelectOptionForm()
    })
