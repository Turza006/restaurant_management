from rest_framework import serializers

from .models import Restaurant_package

class Restaurant_packageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_package
        fields = '__all__'