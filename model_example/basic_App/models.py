from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=128,unique=True)
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    category = models.ForeignKey(Topic)
    name     = models.CharField(max_length=128)
    url      = models.URLField()

    def __str__(self):
        return self.name
