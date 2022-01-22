from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from restapi.serializers import *
from accounts.models import User
from base.models import MallsList, MallsItem, Category



    # ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def helloAPI(request):
    return Response("Hello world!")


@api_view(['GET'])  #쇼핑몰 리스트
def mallsList(request):
    totalmalls = MallsList.objects.all()
    serializer = MallsListSerializer(totalmalls, many=True)
    return Response(serializer.data)


@api_view(['GET'])  #쇼핑몰의 아이템들
def mallsItems(request, pk):
    try:
        mallsitems = MallsItem.objects.filter(id=pk)
        serializer = MallsItemSerializer(mallsitems, many=True)
        return Response(serializer.data)
    except:
        return Response("id 가 존재하지 않습니다.")


@api_view(['GET'])  #모든 상품
def itemList(request):
    totalitems = MallsItem.objects.all()
    serializer = MallsItemSerializer(totalitems, many=True)
    return Response(serializer.data)


@api_view(['POST'])  #쇼핑몰 create
def mallsCreate(request):
    serializer = MallsListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST', 'GET'])  #쇼핑몰 update
def mallsUpdate(request, pk):
    try:
        if request.method == 'GET':
            mall = MallsList.objects.get(id=pk)
            serializer = MallsListSerializer(mall, many=False)
            return Response(serializer.data)

        elif request.method == 'POST':
            mall = MallsList.objects.get(id=pk)
            serializer = MallsListSerializer(instance=mall, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)
    except:
        return Response("id 가 존재하지 않습니다.")


@api_view(['DELETE', 'GET'])  #쇼핑몰 delete
def mallsDelete(request, pk):
    try:
        if request.method == 'GET':
            mall = MallsList.objects.get(id=pk)
            serializer = MallsListSerializer(mall, many=False)
            return Response(serializer.data)

        elif request.method == 'DELETE':
            mall = MallsList.objects.get(id=pk)
            mall.delete()
            return Response("mall succsesfully delete!")
    
    except:
        return Response("id 가 존재하지 않습니다.")


# 아이템들 ---------------------------------------------
@api_view(['POST'])  #쇼핑몰의 아이템 create
def itemCreate(request, pk):
    try:
        serializer = MallsItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    except:
        return Response("id 가 존재하지 않습니다.")


@api_view(['POST', 'GET'])  #아이템 update
def itemUpdate(request, pk, num):
    try:
        if request.method == 'GET':
            item = MallsItem.objects.get(id=pk, num=num)
            serializer = MallsItemSerializer(item, many=False)
            return Response(serializer.data)

        elif request.method == 'POST':
            item = MallsItem.objects.get(id=pk, num=num)
            serializer = MallsItemSerializer(instance=item, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)
    except:
        return Response("id와 number을 확인해주세요.")



@api_view(['DELETE', 'GET'])  #아이템 delete
def itemDelete(request, pk, num):
    try:
        if request.method == 'GET':
            item = MallsItem.objects.get(id=pk, num=num)
            serializer = MallsItemSerializer(item, many=False)
            return Response(serializer.data)

        elif request.method == 'DELETE':
            mall = MallsItem.objects.get(id=pk, num=num)
            mall.delete()
            return Response("item succsesfully delete!")
    
    except:
        return Response("id와 number을 확인해주세요.")



# generics 뷰 이용해보기 --------------------------------------
class mallView(generics.CreateAPIView):
    queryset = MallsList.objects.all()
    serializer_class = MallsListSerializer

class mallListView(generics.ListAPIView):
    queryset = MallsList.objects.all()
    serializer_class = MallsListSerializer