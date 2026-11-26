from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.BigIntegerField(max_length=10)
    my_email = models.EmailField()


    def __str__(self):
        return f" {self.name} - {self.email}"


class Department(models.Model):
    name= models.CharField(max_length=20,unique=True) 


    def __str__(self):
        return self.name   


class Enmployee(models.Model):
    name = models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    salary= models.DecimalField(max_digits=10,decimal_places=2)
    depart=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="employeeeeee")
