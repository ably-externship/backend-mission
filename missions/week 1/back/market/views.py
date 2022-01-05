from django.shortcuts import render

from django.views.generic.base import View, TemplateView
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, 'market/market_list.html')

def detail(request, market_id):
    context = {'market': market_id}
    return render(request, 'market/market_detail.html', context)

