from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .serializers import TodoSerializer
from .models import Todo

class TodoGeneralView(APIView) :


    def get(self, request) -> Response:

        qs = Todo.objects.all()
        serializer = TodoSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request) -> Response:

        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class TodoSepcView(APIView) :

    def find_by_pk(self, pk) :
        try :
            return Todo.objects.get(pk=pk)
        except :
            raise Http404


    def put(self, request, pk) -> Response:

        todo = self.find_by_pk(pk)
        serializers = TodoSerializer(todo, data=request.data)

        if serializers.is_valid() :
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk) -> Response:

        todo = self.find_by_pk(pk)
        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

