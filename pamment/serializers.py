from rest_framework import serializers

from .models import Pamment

class PammentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pamment
        fields = '__all__'