from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from student.models import * 

class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]

class signinForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields = '__all__'





       