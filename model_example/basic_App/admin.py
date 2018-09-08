from django.contrib import admin

# Register your models here.
from basic_App.models import Topic,Webpage

admin.site.register(Topic)
admin.site.register(Webpage)
