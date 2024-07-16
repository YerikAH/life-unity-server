from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
  image = models.ImageField(upload_to='images/users/', blank=True, null=True)
  email = models.EmailField(unique=True)
  
  class Meta:
    db_table = 'users'