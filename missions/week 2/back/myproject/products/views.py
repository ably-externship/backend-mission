from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Q

from .models import *

# Create your views here.


def detail_view(request):
    products = Product.objects.first()
    board = Board.objects.all()

    return render(request, "detail.html", {"products": products, "board": board})


def main(request):
    products = Product.objects.all()

    paginator = Paginator(products, 2)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(
        request,
        "main.html",
        {
            "products": products,
            "posts": posts,
        },
    )


def searchItem(request):
    keyword = request.GET.get("search", "")
    products = Product.objects.filter(
        Q(name__icontains=keyword) | Q(description__icontains=keyword)
    )

    paginator = Paginator(products, 10)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(
        request,
        "search.html",
        {
            "products": products,
            "posts": posts,
        },
    )


def post_search(request):
    return render(request, "search.html")
