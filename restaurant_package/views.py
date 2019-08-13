from django.shortcuts import render
from .models import Restaurant_package
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Restaurant_packageSerializer

# Create your views here.
class Restaurant_package_List(APIView):
    def get(self,request):
        data = Restaurant_package.objects.all()
        serializer = Restaurant_packageSerializer(data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Restaurant_packageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
