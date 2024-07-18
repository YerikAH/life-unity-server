from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import NutritionPersonalDetails, ValuesConsumedPerDay
from .serializers import NutritionPersonalDetailsSerializer, ValuesConsumedPerDaySerializer

# Create your views here.
class NutritionPersonalDetailsViewSet(ModelViewSet):
    queryset = NutritionPersonalDetails.objects.all()
    serializer_class = NutritionPersonalDetailsSerializer
    permission_classes = [IsAuthenticated]
    

class ValuesConsumedPerDayViewSet(ModelViewSet):
    queryset = ValuesConsumedPerDay.objects.all()
    serializer_class = ValuesConsumedPerDaySerializer
    permission_classes = [IsAuthenticated]