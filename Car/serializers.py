from .models import *
from rest_framework import serializers


class CarOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOnline
        fields = '__all__'


class ReviewCar(serializers.ModelSerializer):
    class Meta:
        model = ReviewCom
        fields = '__all__'
