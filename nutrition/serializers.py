from rest_framework.serializers import ModelSerializer
from .models import NutritionPersonalDetails, ValuesConsumedPerDay

class NutritionPersonalDetailsSerializer(ModelSerializer):
    class Meta:
        model = NutritionPersonalDetails
        fields = "__all__"

class ValuesConsumedPerDaySerializer(ModelSerializer):
    class Meta:
        model = ValuesConsumedPerDay
        fields = "__all__"
      