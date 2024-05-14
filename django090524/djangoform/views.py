from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def studentForm(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            roll_number = fm.cleaned_data['roll_number']
            age = fm.cleaned_data['age']
            address = fm.cleaned_data['address']
            #save to model
            # student = Student(name=name, roll_number=roll_number, age=age, address=address)
            # student.save()
            print(name, roll_number)
            return redirect('student-form')
    fm = StudentForm()
    return render(request, 'djangoform/studentDetails.html', {'form':fm})