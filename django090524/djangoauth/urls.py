
from django.urls import path
from . import views 

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.user_logout, name='logout'),
    ]