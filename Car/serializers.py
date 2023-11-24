from .models import *
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOnline
        fields = '__all__'
