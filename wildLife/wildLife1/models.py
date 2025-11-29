from django.db import models

# Create your models here.

class Animals(models.Model):
    name =models.CharField()
    description=models.CharField(max_length=255)
    reserve=models.CharField()
    picture=models.CharField()
    number=models.IntegerField()


    def __str__(self):
       return self.name