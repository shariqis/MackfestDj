from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=(
        "first_name",
        "age",
        "my_email"
    )

    search_fields=(
        "first_name",
        "age"
    )

    ordering=("id",)
