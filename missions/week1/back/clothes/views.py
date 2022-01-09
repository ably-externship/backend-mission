from re import template
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import View, DetailView, FormView
import random
from . import models, forms


def all_clothes(request):
    clothes_set = set()
    uppers = models.Upper.objects.all()
    outers = models.Outers.objects.all()
    onepieces = models.Onepieces.objects.all()
    len_uppers = len(uppers)
    len_outers = len(outers)
    len_onepieces = len(onepieces)
    if len_uppers + len_outers + len_onepieces <= 12:
        clothes_set.update(uppers[:len_uppers])
        clothes_set.update(outers[:len_outers])
        clothes_set.update(onepieces[:len_onepieces])
        return render(
            request,
            "clothes/home.html",
            context={
                "clothes_set": clothes_set,
                "uppers": uppers,
                "outers": outers,
                "onepieces": onepieces,
            },
        )
    else:
        while True:
            clothes_set.add(uppers[random.randint(0, len_uppers - 1)])
            clothes_set.add(outers[random.randint(0, len_outers - 1)])
            clothes_set.add(onepieces[random.randint(0, len_onepieces - 1)])
            if len(clothes_set) == 12:
                break
        return render(
            request,
            "clothes/home.html",
            context={
                "clothes_set": clothes_set,
                "uppers": uppers,
                "outers": outers,
                "onepieces": onepieces,
            },
        )


def Uppers_views(request):
    page = request.GET.get("page", 1)
    uppers_list = models.Upper.objects.all()
    paginator = Paginator(uppers_list, 10)
    try:
        uppers = paginator.get_page(page)
        return render(
            request,
            "clothes/upper_list.html",
            context={"uppers": uppers},
        )
    except EmptyPage:
        return redirect("/")  # home으로 이동


def Outers_views(request):
    page = request.GET.get("page", 1)
    outers_list = models.Outers.objects.all()
    paginator = Paginator(outers_list, 10)
    try:
        outers = paginator.get_page(page)
        return render(request, "clothes/outer_list.html", context={"outers": outers})
    except EmptyPage:
        return redirect("/")


def Onepieces_views(request):
    page = request.GET.get("page", 1)
    onepieces_list = models.Onepieces.objects.all()
    paginator = Paginator(onepieces_list, 10)
    try:
        onepieces = paginator.get_page(page)
        return render(
            request, "clothes/onepiece_list.html", context={"onepieces": onepieces}
        )
    except EmptyPage:
        return redirect("/")


class Upper_detail(DetailView):
    model = models.Upper


def Outer_detail(request, pk):
    outer = models.Outers.objects.get(pk=pk)
    return render(request, "clothes/outer_detail.html", context={"outer": outer})


def Onepiece_detail(request, pk):
    onepiece = models.Onepieces.objects.get(pk=pk)
    return render(
        request, "clothes/onepiece_detail.html", context={"onepiece": onepiece}
    )


class SearchFormView(FormView):
    form_class = forms.SearchForm
    template_name = "clothes/search.html"

    def form_valid(self, form):
        word = "%s" % self.request.GET["word"]
        clothes_list = models.Upper.filter(
            Q(title__icontains=word) | Q(content__icontains=word)
        ).distinct()
        context = {}
        context["object_list"] = clothes_list
        context["search_word"] = word
        return context
