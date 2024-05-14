from django.db import models

# one to one 
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#one to many
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    
# many to many
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    subject = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    student = models.ManyToManyField(Student)
    
    #custome function to create a list of student having same subject
    def student_list(self):
        return ','.join([str(stu) for stu in self.student.all()])