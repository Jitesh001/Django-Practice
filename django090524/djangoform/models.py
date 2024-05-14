from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    roll_number = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=100)
