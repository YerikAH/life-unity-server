from django.db import models
from authentication.models import UserModel

# Create your models here.
class NutritionPersonalDetails(models.Model):
  id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='id_user',null=True)
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

class ValuesRecommendedPerDay(models.Model):
  id_nutrition_personal_details = models.ForeignKey(NutritionPersonalDetails, on_delete=models.CASCADE, db_column='id_nutrition_personal_details', null=True)
  carbs = models.FloatField(null=True)
  protein = models.FloatField(null=True)
  fat = models.FloatField(null=True)
  cals = models.FloatField(null=True)
  water_liters = models.FloatField(null=True)
  water_cups = models.IntegerField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = 'values_recommended_per_day'
    
  def __str__(self):
    return self.id_nutrition_personal_details

class ValuesConsumedPerDay(models.Model):
  id_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, db_column='id_user',null=True)
  total_carbs = models.FloatField(null=True, default=0)
  total_protein = models.FloatField(null=True, default=0)
  total_fat = models.FloatField(null=True, default=0)
  total_cals = models.FloatField(null=True, default=0)
  total_water = models.FloatField(null=True, default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = 'values_consumed_per_day'
    
  def __str__(self):
    return str(self.id_user.first_name)