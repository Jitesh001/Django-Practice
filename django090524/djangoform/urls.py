from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentForm, name='student-form'),
]
