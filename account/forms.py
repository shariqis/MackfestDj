
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .models import StudentFile, Student


class RegistratiomForm(UserCreationForm):
    email=forms.EmailField(required=True)

    role=forms.ChoiceField(choices=[
        ('student','Student'),
        ('teacher','Teacher')
    ])

    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'role'
        
        ]

    def clean_email(self):
        email  =self.cleaned_data['email']  

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('This email already registered....')

        return email
    


class StudentFileForm(forms.ModelForm):
    class Meta:
        model=StudentFile
        fields=[
            'title',
            'file'
        ]   
    


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=[
            'name',
            'email',
            'course'
        ]