from django.db import models
from mainapp import settings


class employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_salary = models.IntegerField()
    hr_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

