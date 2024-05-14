from django.db import models

#Abstract Model Inheritance
class CommonFields(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True
    
class Student(CommonFields):
    roll_number = models.IntegerField()
    date = None
#Student table column [name, age, roll_number], no date column as it set as None

class Teacher(CommonFields):
    salary = models.IntegerField()
#Teacher table column [name, age, date, salary]

class Contractor(CommonFields):
    date = models.DateTimeField()
    duration = models.IntegerField()
#Contractor table column [name, age, date(date-time format), duration]  


#Multi-Table Inheritance
class ExamCenter(models.Model):
    city = models.CharField(max_length=100)
    city_code = models.IntegerField()
#ExamCenter table column [id, city, city_code]

class Candidate(ExamCenter):
    name = models.CharField(max_length=100)
    sr_number = models.IntegerField()
#Candidate table column [id, city, city_code, name, sr_number] 
#here id is django created id which will be common in both table, indicating PK from ExamCenter table


#proxy model exmple 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    
class CopyProduct(Product):
    class Meta:
        proxy = True
        ordering = ['id']
        
#both above models have same single table, but the behavior on admin panel will change.
#for Product the items will be display in descening ID order while for CopyProduct in ascending ID order