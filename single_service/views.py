from django.shortcuts import render
from .models import Single_service
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Single_serviceSerializer

# Create your views here.
class Single_service_list(APIView):
    def get(self,request):
        data = Single_service.objects.all()
        serializer = Single_serviceSerializer(data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = Single_serviceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

