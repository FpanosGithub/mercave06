from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    organizacion = models.CharField(max_length=20, null= True, blank = True)
    pass