from django import forms
from .models import Student
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):

    class Meta:#meta is keyword 
        model=Student
        fields=['name','roll']
        
   