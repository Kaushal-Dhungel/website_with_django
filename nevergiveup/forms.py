from django import forms
from .models import mydatabase
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class UserForm(forms.ModelForm):
    
    username = forms.IntegerField(label ='phone')
    password = forms.CharField(widget = forms.PasswordInput())
    #password2 =forms.CharField(widget = forms.PasswordInput()) 
    
    
    class Meta:
        model = User
        
        fields = ('username','email','password','first_name')
        #labels = {
        #    "username": "phone"
        #}

        
   
        
    
class CustomForm(forms.ModelForm):
    groups = [
        
        ('A +ve','A +ve'),
        ('B +ve','B +ve'),
        ('AB +ve','AB +ve'),
        ('O +ve','O +ve'),
        ('A -ve','A -ve'),
        ('B -ve','B -ve'),
        ('AB -ve','AB -ve'),
        ('O -ve','O -ve')
    ]
    
    
    address = [
        
        
        ('Jhapa','Jhapa'),
        ('Illam','Illam'),
        ('Morang','Morang'),
        ('Kathmandu','Kathmandu'),
        ('Chitwan','Chitwan'),
        ('Kapilbastu','Kapilbastu'),
        ('Sunsari','Sunsari'),
        ('Kaski','Kaski'),
        ('Hisar','Hisar')
    ]
    location = forms.CharField(widget = forms.Select(choices = address))
    b_group = forms.CharField(widget = forms.Select(choices = groups))
    
    class Meta:
        model = mydatabase
        fields = ('location','b_group')