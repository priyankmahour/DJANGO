from django.contrib import admin

# Register your models here.
from basic_App.models import Company

class AdminCompany(admin.ModelAdmin):
    list_display = ['id','name','location','date']

admin.site.register(Company,AdminCompany)
