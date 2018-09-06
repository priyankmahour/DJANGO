from django.contrib import admin

# Register your models here.
from basic_app.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','marks']

admin.site.register(Student,StudentAdmin)
