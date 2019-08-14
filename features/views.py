from django.shortcuts import render
from .models import Features
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FeaturesSerializer

# Create your views here.
class featureslist(APIView):
    def get(self,request):
        data = Features.objects.all()
        serializer = FeaturesSerializer(data,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = FeaturesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
