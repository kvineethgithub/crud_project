from django.db import models
from django.utils import timezone

class Employee(models.Model):
    employee_name=models.CharField(max_length=40)
    employee_email=models.EmailField(max_length=30)
    employee_pic=models.FileField(upload_to='images/%Y/%m/%d')
    def __str__(self):
        return self.employee_name