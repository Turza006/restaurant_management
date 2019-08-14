from django.shortcuts import render
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer

# Create your views here.
class Item_List(APIView):
    def get(self,request):
        data = Item.objects.all()
        serializer = ItemSerializer(data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
