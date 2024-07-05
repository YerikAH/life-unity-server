from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NutritionPersonalDetails(models.Model):
  id_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_user')
  weight = models.FloatField()
  height = models.FloatField()
  birth_date = models.DateField()
  daily_activity = models.CharField(max_length=50, choices=[
    ('sedentary', 'Sedentary'),
    ('light', 'Light'),
    ('moderate', 'Moderate'),
    ('high', 'High'),
  ])
  sex = models.CharField(max_length=50, choices=[
    ('male', "Male"),
    ('female','Female'),
  ])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'nutrition_personal_details'
  
  def __str__(self):
    return self.id_user

class ValuesConsumedPerDay(models.Model):
  id_nutrition_personal_details = models.ForeignKey(NutritionPersonalDetails, on_delete=models.CASCADE, db_column='id_nutrition_personal_details')
  total_carbs = models.FloatField()
  total_protein = models.FloatField()
  total_fat = models.FloatField()
  total_cals = models.FloatField()
  total_water = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = 'values_consumed_per_day'
    
  def __str__(self):
    return self.id_nutrition_personal_details