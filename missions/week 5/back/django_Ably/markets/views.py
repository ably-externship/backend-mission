from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from collections import defaultdict



# Create your views here.

def page(request):
    store_list = Store.objects.all()
    # # store_list 페이징 처리
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    paginator = Paginator(store_list, '3') #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    print('-----------',page_obj.object_list)
    # print(page)
    return render(request, 'post_list.html', {'page_obj':page_obj})


def post_RedStore(request):
    get_data = request.GET
    print(get_data['store'])
    all_store_obj = Store.objects.all()

    all_id = [all_store_obj[i].id_store for i in range(len(all_store_obj))]
    all_name = [all_store_obj[i].name for i in range(len(all_store_obj))]
    # print(all_id) # S0001, S0002, ...

    item_name_obj = set()
    store_dict = defaultdict(list)
    for id in all_id:
        temp = Item.objects.filter(store_id_store='{}'.format(id)) # QuarySet
        for idx in range(len(temp)):
            item_name_obj.add((id,temp[idx].name)) # temp[idx.name] = QuarySet[0].name, QuarySet[1].name ...        
    item_name_obj = list(item_name_obj)

    for k,v in item_name_obj:
        store_dict[Store.objects.filter(id_store=k)[0].name].append(v)
    
    print('store_key',store_dict.keys())
    
    # print('item_name_obj:',item_name_obj)
    # return render(request, 'red_store.html', store_dict)
    return render(request, 'red_store.html', {'store_item' :store_dict['{}'.format(get_data['store'])],'store_name':[get_data['store']]})



def post_RedShirt(request):
    print('post_get',request.GET)
    items = Item.objects.filter(name='RedShirt')
    colors=set()
    sizes=[]
    for item in items:
        colors.add(item.color)
        sizes.append(item.size)
    colors = list(colors)
    context = {'colors':colors,'sizes':sizes} 
    return render(request,'red_shirt.html', context)

def post_RedSkirt(request):
    return render(request,'red_skirt.html')

def post_RedDress(request):
    return render(request,'red_dress.html')

@permission_classes((IsAuthenticated,))
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('id_item')
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticated]


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all().order_by('id_store')
    serializer_class = StoreSerializer
    # permission_classes = [permissions.IsAuthenticated]


def add_items(request):
    print(request.GET)
    print(request.POST.get)
    get_id = request.POST.get('id_item')
    get_name = request.POST.get('name')
    get_size = request.POST.get('size')
    get_color = request.POST.get('color')
    get_price = request.POST.get('price')
    get_stock = request.POST.get('stock')
    store_id = Store.objects.get(id_store ='S0001')
    new_item = Item.objects.create(
        id_item = get_id,
        name = get_name,
        size = get_size,
        color = get_color,
        price = get_price,
        stock = get_stock,
        store_id_store = store_id
    )
    return redirect('/redstore/items')



def update_items(request,pk):
    get_name = request.POST.get('name')
    get_size = request.POST.get('size')
    get_color = request.POST.get('color')
    get_price = request.POST.get('price')
    get_stock = request.POST.get('stock')

    store_items = Item.objects.get(id_item=pk)
    store_items.name = get_name
    store_items.size = get_size
    store_items.color = get_color
    store_items.price = get_price
    store_items.stock = get_stock

    store_items.save()

    return redirect('/redstore/items')


def delete_items(request,pk):
    items = Item.objects.filter(store_id_store = 'S0001')
    store_items = items.get(id_item=pk)

    store_items.delete()
    return redirect('/redstore/items')


    


