from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from markets.models import Market
from .models import Product, ProductOption, Category
from .forms import SearchForm, QuestionForm
from .serializers import ProductSerializer, ProductOptionSerializer


class ProductListView(ListView):
    model = Product
    paginate_by = 12
    ordering = "created_at"
    template_name = 'home.html'
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product


def search(request):
    product_name = request.GET.get('name')
    if product_name:
        form = SearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            products = Product.objects.filter(name__icontains=name).order_by("-created_at")
            return render(request, 'products/search.html', {'form': form, 'products': products})
    else:
        form = SearchForm()
    return render(request, 'products/search.html', {'form': form})


@login_required(login_url='users:login')
def question(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.product = product
            question.save()
            return redirect(question)
    else:
        form = QuestionForm()
    return render(request, 'products/question.html', {'form': form, 'product': product})


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('market', 'category')
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        관리자가 마켓이름, 카테고리를 입력했을 때
        DB에 해당 내용이 있으면 해당 데이터의 값을 넣고 없으면 생성 후 해당 데이터를 넣습니다.
        """

        market_name = self.request.data['market']
        category_name = self.request.data.get('category', None)

        market, _ = Market.objects.get_or_create(name=market_name)
        category, _ = Category.objects.get_or_create(name=category_name)

        serializer.save(market=market, category=category)


# 한 API 에서 상품 옵션까지 다 추가 할 수 있도록 구성
class ProductAPIView(APIView):
    """상품 리스트 조회, 추가 API"""
    def get(self, request, *args, **kwargs):
        products = Product.objects.select_related('category', 'market')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # 기본 제품 생성
        market_name = self.request.data['market']
        category_name = self.request.data.get('category', None)
        name = self.request.data['name']
        price = self.request.data['price']

        market, _ = Market.objects.get_or_create(name=market_name)
        category, _ = Category.objects.get_or_create(name=category_name)
        product = Product.objects.create(name=name, price=price, market=market, category=category)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 제품 / 옵션 각각 API 분리
class ProductDetailAPIView(APIView):
    """제품 상세 조회, 수정, 삭제 API"""
    def get(self, request, **kwargs):
        product_id = self.kwargs['pk']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': '해당 제품은 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, **kwargs):
        product_id = self.kwargs['pk']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': '해당 제품은 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        name = self.request.data.get('name', None)
        price = self.request.data.get('price', None)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': '해당 제품은 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

        if name is not None:
            product.name = name
        if price is not None:
            product.price = price

        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductOptionAPIView(APIView):
    """제품 옵션 조회, 생성 API"""
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        options = ProductOption.objects.filter(product_id=product_id)
        if options:
            serializer = ProductOptionSerializer(options, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        color = self.request.data.get('color', None)
        size = self.request.data.get('size', None)
        stock = self.request.data.get('stock', None)

        # 기존 제품에 이미 있는 옵션이면 수량만 수정됨
        option, created = ProductOption.objects.get_or_create(product_id=product_id, color=color, size=size)

        if created:
            option.stock = stock
            option.save()
            serializer = ProductOptionSerializer(option)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': '이미 있는 옵션입니다.'}, status=status.HTTP_400_BAD_REQUEST)


class ProductOptionDetailAPIView(APIView):
    """제품 옵션 상세조회, 수정, 삭제 API"""
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs['pk']
        options = ProductOption.objects.filter(product_id=product_id)
        if options:
            serializer = ProductOptionSerializer(options, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        """
        프론트에서 debounce 처리가 되어 있지 않다면
        여러번 클릭 시 없는 제품을 삭제요청을 하기 때문에 예외처리 하였습니다.
        """
        option_id = self.kwargs['option_id']
        try:
            option = ProductOption.objects.get(id=option_id)
        except ProductOption.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        option.delete()
        return Response({'error': '해당 제품은 없습니다.'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        option_id = self.kwargs['option_id']
        color = self.request.data.get('color', None)
        size = self.request.data.get('size', None)
        stock = self.request.data.get('stock', 1)
        add_price = self.request.data.get('add_price', False)
        is_sold_out = self.request.data.get('is_sold_out', False)

        option = ProductOption.objects.get(id=option_id)
        option.color = color
        option.size = size
        option.stock = stock
        option.add_price = add_price
        option.is_sold_out = is_sold_out
        option.save()
        serializer = ProductOptionSerializer(option)
        return Response(serializer.data, status=status.HTTP_200_OK)
