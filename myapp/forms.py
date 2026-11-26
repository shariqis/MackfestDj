from django import forms

from .models import Student,Enmployee,Department


class StudentModelForm(forms.ModelForm):
    class Meta:
        model= Student

        fields='__all__'


        labels={
            "first_name":"ENTER FIRST NAME"
        }

        # help_texts={
        #     "age":"Choose ur dob"
        # }

        # fields=['name','age']
        # exclude=['name','age']


class EmpModelForm(forms.ModelForm):
    class Meta:
        model= Enmployee

        fields="__all__"       

        widgets={
            "name":
            forms.TextInput(attrs={
                "class":
                "form-control",
                "placeholder":"Enter Employee Name"
            }),
            "email":
                    forms.EmailInput(attrs={
                        "class":
                        "form-control",
                        "placeholder":"Enter Email address"
                    }),
                    "salary":
                            forms.NumberInput(attrs={
                                "class":
                                "form-control",
                                "placeholder":"Enter Salary"
                            }),
                            "depart":
                                    forms.Select(attrs={
                                        "class":
                                        "form-select"
                                        
                                    }),
        }