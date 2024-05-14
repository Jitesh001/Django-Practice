from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=150)
#     roll_number = forms.IntegerField()
#     age = forms.IntegerField()
#     address = forms.CharField(max_length=100)
    
#using modelfom
class StudentForm(forms.ModelForm):
    name = forms.CharField(max_length=150, required=False) 
    #validation for name fields, more prioity then model field
    class Meta:
        model = Student
        fields = ['name', 'age', 'address', 'roll_number']
        labels = {'name':'Enter your Name', 'age':'Enter your Age'}
        error_messages = {'name':{'required':'Bhai NAME toh Likho'}}