from django.contrib import admin
from api.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "roll", "city"]


# Register your models here.
