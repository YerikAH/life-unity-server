from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import NutritionPersonalDetails, ValuesConsumedPerDay
from .serializers import NutritionPersonalDetailsSerializer, ValuesConsumedPerDaySerializer

# Create your views here.
class NutritionPersonalDetailsViewSet(ModelViewSet):
    queryset = NutritionPersonalDetails.objects.all()
    serializer_class = NutritionPersonalDetailsSerializer

class ValuesConsumedPerDayViewSet(ModelViewSet):
    queryset = ValuesConsumedPerDay.objects.all()
    serializer_class = ValuesConsumedPerDaySerializer   