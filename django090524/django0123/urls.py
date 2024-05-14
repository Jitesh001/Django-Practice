from django.urls import path
from . import views 

urlpatterns = [
    path('index', views.page_index1, name='page-index1'),
    ]