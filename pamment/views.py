from django.shortcuts import render
from .models import Pamment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PammentSerializer

# Create your views here.
class Pamment_List(APIView):
    def get(self,request):
        data = Pamment.objects.all()
        serializer = PammentSerializer(data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PammentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
