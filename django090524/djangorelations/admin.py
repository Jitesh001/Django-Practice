from django.contrib import admin
from .models import User, Department, Singer, Song, Student, Subject

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'role']
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
   list_display = ['id', 'dept_name', 'dept_desc', 'user']
   
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'gender', 'city']
   
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
   list_display = ['id', 'title', 'duration', 'singer']
   
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'age']
   
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
   list_display = ['id', 'subject', 'total_marks', 'student_list']
   #student_list is a custome function to display student lists