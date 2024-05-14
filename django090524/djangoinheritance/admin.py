from django.contrib import admin
from .models import Student, Teacher, Contractor, ExamCenter, Candidate, Product, CopyProduct
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Contractor)

@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'city_code']
    
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'city_code', 'name', 'sr_number']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'category']
    
@admin.register(CopyProduct)
class CopyProductAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'price', 'category']