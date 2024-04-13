from rest_framework.generics import ListAPIView

from app_cafe.models import Hotdog, Drink, Spicy
from app_cafe.serializers import HotdogSerializer, DrinkSerializer, SpicySerializer


class HotdogListAPIView(ListAPIView):
    queryset = Hotdog.objects.all()
    serializer_class = HotdogSerializer


class DrinkListAPIView(ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer


class SpicyListAPIView(ListAPIView):
    queryset = Spicy.objects.all()
    serializer_class = SpicySerializer