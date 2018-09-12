from django.db import models

# Create your models here.

class Company(models.Model):
    name      = models.CharField(max_length=128)
    location  = models.CharField(max_length=128)
    date      = models.DateField()

    
