from django.shortcuts import render

from django.core.paginator import Paginator
from .models import *

# Create your views here.
def test_view(request):
    return render(request, "nav.html")


def detail_view(request):
    products = Product.objects.first()
    board = Board.objects.all()

    return render(request, "detail.html", {"products": products, "board": board})


def bottom_view(request):
    products = Product.objects.all()

    paginator = Paginator(products, 2)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    return render(
        request,
        "bottom.html",
        {
            "products": products,
            "posts": posts,
        },
    )
