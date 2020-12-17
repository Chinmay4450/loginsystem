from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class hrAccounts(AbstractUser):
      name = models.CharField(max_length=70)
      username = models.CharField(max_length=70, unique=True)
      password = models.CharField(max_length=70)
      name = models.CharField(max_length=70)