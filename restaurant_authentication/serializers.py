from rest_framework import serializers

from .models import Restaurant_description

class Restaurant_descriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_description
        fields = '__all__'