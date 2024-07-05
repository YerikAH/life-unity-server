from django.db import models

# Create your models here.
class RecipesViewSet(models.Model):
  name = models.CharField(max_length=255, null=False, blank=False)
  description = models.TextField(null=False, blank=True)
  link = models.TextField(null=False, blank=False)
  type_meal = models.CharField(max_length=50, choices=[
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('snack', 'Snack'),
    ('dessert', 'Dessert'),
  ])
  cals_kcal = models.FloatField(default=0.0, null=False, blank=True)
  protein_g = models.FloatField(default=0.0, null=False, blank=True)
  carbs_g = models.FloatField(default=0.0, null=False, blank=True)
  fat_g = models.FloatField(default=0.0, null=False, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    db_table = 'recipes'