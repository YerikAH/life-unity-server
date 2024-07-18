from rest_framework.serializers import ModelSerializer
from .models import NutritionPersonalDetails, ValuesConsumedPerDay, ValuesRecommendedPerDay

class NutritionPersonalDetailsSerializer(ModelSerializer):
    class Meta:
        model = NutritionPersonalDetails
        fields = "__all__"

class ValuesConsumedPerDaySerializer(ModelSerializer):
    class Meta:
        model = ValuesConsumedPerDay
        fields = "__all__"
        
class ValuesRecommendedPerDaySerializer(ModelSerializer):
    class Meta:
        model = ValuesRecommendedPerDay
        fields = "__all__"
      