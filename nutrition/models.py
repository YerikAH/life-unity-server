from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NutritionPersonalDetails(models.Model):
  id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user')
  weight = models.FloatField()
  height = models.FloatField()
  birth_date = models.DateField()
  daily_activity = models.CharField(max_length=50, choices=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"])
  sex = models.CharField(max_length=50, choices=["Male", "Female"])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'nutrition_personal_details'

class ValuesConsumedPerDay(models.Model):
  id_nutrition_personal_details = models.ForeignKey(NutritionPersonalDetails, on_delete=models.CASCADE, db_column='id_nutrition_personal_details')
  total_carbs = models.FloatField()
  total_protein = models.FloatField()
  total_fat = models.FloatField()
  total_cals = models.FloatField()
  total_water = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)