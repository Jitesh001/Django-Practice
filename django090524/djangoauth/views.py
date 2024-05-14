from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomeUserForm
from django.contrib import messages #django messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .signals import notification
# Create your views here.

#method1 - using only UserCreationForm
def sign_up(request):
    notification.send(sender=None, request=request, user=['user1', 'user2']) #cusom signal demo
    messages = None
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            print('success')
            #userForm.save() 
            #logic for adding user to Post Manager group when sign up
            user = userForm.save()
            group = Group.objects.get(name='Post Manager')
            user.groups.add(group)
            #adding group logic ends
            messages = ['User Created Successfully']
    else:
        userForm = UserCreationForm()
    return render(request, 'djangoauth/signup.html', {'form':userForm, 'messages':messages})

#method2 - using customized form inheriting UserCreationForm and User Model
def customised_sign_up(request):
    messages = None
    if request.method == 'POST':
        userForm = CustomeUserForm(request.POST)
        if userForm.is_valid():
            messages.success(request, 'Account Created Successfully!')
            print('success')
            userForm.save()
    else:
        userForm = CustomeUserForm()
    return render(request, 'djangoauth/signup.html', {'form':userForm})

#use one of above form view one at time in urls.py for path 'signup/' to see the difference

def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'djangoauth/home.html')
    return redirect('login')
#authentication views

#login
def user_login(request):
    #if user is not authenticated then redirect to login else redirect to Home page
    if not request.user.is_authenticated:
        if request.method == 'POST':
            loginForm = AuthenticationForm(request=request, data=request.POST)
            if loginForm.is_valid():
                uname = loginForm.cleaned_data['username']
                upwd = loginForm.cleaned_data['password']
                user = authenticate(username=uname, password=upwd)
                if user is not None:
                    login(request, user)
                    return render(request, 'djangoauth/home.html', {'user':request.user})
                    
        loginForm = AuthenticationForm()
        return render(request, 'djangoauth/login.html', {'form':loginForm})
    else:
        return redirect('home')

#logout
def user_logout(request):
    logout(request)
    return redirect('login')