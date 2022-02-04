from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Product, ProductOptionGroup, ProductOptionGroupItem, ProductImg, ProductStock
from .serializers import ProductSerializer,ProductImgSerializer

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from .pagination import DashboardPageNumberPagination


@csrf_exempt
def itemIndex(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        posts = paginator.get_page(page)
        serializer = ProductSerializer(posts, many=True)
        return render(request, 'ALLproduct.html', {'product_list': posts})

@csrf_exempt
def allItem(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        products = Product.objects.all()
        paginator = Paginator(products, 3)
        posts = paginator.get_page(page)
        serializer = ProductSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def itemSearch(request):
    if request.method == 'POST':
        item_search = request.POST.get('item_search')
        result = Product.objects.filter(product_name__contains=item_search)

        serializer = ProductSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)



from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status, generics

from django.utils.deprecation import MiddlewareMixin

class DisableCsrfCheck(MiddlewareMixin):

    def process_request(self, req):
        attr = '_dont_enforce_csrf_checks'
        if not getattr(req, attr, False):
            setattr(req, attr, True)


# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')

# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @authentication_classes((JWTAuthentication,))
class BillingRecordsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   # pagination_class = DashboardPageNumberPagination



class ProductViewSet(viewsets.ViewSet):

    @csrf_exempt
    def list(self, request):  # /api/shop
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/shop
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @csrf_exempt
    def retrieve(self, request, pk=None):  # /api/shop/<pk>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductImgViewSet(viewsets.ViewSet):


    @csrf_exempt
    def list(self, request):  # /api/shop

        product = ProductImg.objects.all()
        serializer = ProductImgSerializer(product, many=True)
        return Response(serializer.data)

    def create(self, request):  # /api/shop
        serializer = ProductImgSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @csrf_exempt
    def retrieve(self, request, pk=None):  # pk  product , many
        product = ProductImg.objects.get(product=pk)
        serializer = ProductImgSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = ProductImg.objects.get(id=pk)
        serializer = ProductImgSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = ProductImg.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)