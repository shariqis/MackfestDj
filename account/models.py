from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    ROLE_CHOICES=[
        ('student','Student'),
        ('teacher','Teacher')
    ]

    user= models.OneToOneField(
        User,on_delete=models.CASCADE
    )

    role= models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )


    def __str__(self):
        return f"{self.user.username} - {self.role}"
    


class StudentFile(models.Model):
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    file=models.FileField(upload_to='student_files/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} uploaded by {self.student.username}"
    


class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name 

