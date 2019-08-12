from django.shortcuts import render
from .models import Restaurant_description
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Restaurant_descriptionSerializer



def home(request):

    return render(request,'restaurant_authentication/home.html')



class Restaurant_authenticationList(APIView):
    def get(self,request):
        data = Restaurant_description.objects.all()
        serializer = Restaurant_descriptionSerializer(data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Restaurant_descriptionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
