from django.db import models
from django.contrib.auth.models import AbstractUser
from storages.backends.s3boto3 import S3Boto3Storage

# Define un almacenamiento personalizado para que no se procese 'collectstatic' en este campo
class MediaStorage(S3Boto3Storage):
    location = 'profiles'  # Este es un ejemplo, puedes especificar una ubicación diferente en tu bucket
    file_overwrite = False

# Create your models here.
class UserModel(AbstractUser):
  image = models.ImageField(null=True, storage=MediaStorage(), upload_to='profiles/')
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  
  class Meta:
    db_table = 'users'