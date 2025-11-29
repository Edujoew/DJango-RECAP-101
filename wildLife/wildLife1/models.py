from django.db import models

# Create your models here.

class Animals(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    reserve = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    number = models.IntegerField()


    def __str__(self):
       return self.name