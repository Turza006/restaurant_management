from rest_framework import serializers

from .models import Single_service

class Single_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single_service
        fields = '__all__'