from rest_framework import serializers

from app_cafe.models import Hotdog, Drink, Spicy


class HotdogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotdog
        fields = ['id', 'name', 'cover', 'data_create', 'data_update', 'price']


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'title', 'cover', 'price']


class SpicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Spicy
        fields = ['id', 'level', 'cover']

