from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator 

# Create your views here.
def page(request):
    store_list = Store.objects.all()
    # board_list 페이징 처리
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(store_list, '3') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'template_name', {'page_obj':page_obj})
