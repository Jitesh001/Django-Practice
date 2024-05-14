from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomeUserForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password Again', widget=forms.PasswordInput)
    #customized password2 field from UserCreationForm
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        #all above are User Model Fields, except UserCreationForm will add two pwd fields automatically
        labels = {'emai':'Enter your email'}