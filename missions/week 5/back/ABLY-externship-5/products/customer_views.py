from django.http import request
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from .models import MainCategory, SubCategory, BaseMerchandise, Merchandise
from accounts.tokens import jwt_authorization
from carts.forms import AddMerchandiseForm

# Create your views here.


class HomeView(ListView):
    
    model = BaseMerchandise
    template_name = 'core/home.html'
    context_object_name = 'merchandises'
    paginate_by = 8
    merchandise_list = BaseMerchandise.objects.all()
    user = None
    
    def __init__(self, **kwargs):
        try:
            self.user = self.request.user
        except:
            pass
        super().__init__(**kwargs)
    
    def get_queryset(self):
        if self.request.method == 'GET':
            q = self.request.GET.get('search', '')
            self.merchandise_list = BaseMerchandise.objects.filter(name__icontains=q)
        return self.merchandise_list


class MerchandiseDetail(DetailView):
    
    model = BaseMerchandise
    template_name = 'products/merchandise_detail.html'
    context_object_name = 'merchandise'
    
    def get(self, request, *args, **kwargs):
        add_to_cart = AddMerchandiseForm(initial={'quantity':1})
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        if request.user:
            context['user'] = request.user
        context['option'] = Merchandise.objects.filter(basemerchandise=self.object)[0] # needs dropdown UI & mechandise loop
        context['add_to_cart'] = add_to_cart
        return self.render_to_response(context)