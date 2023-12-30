from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class menuItem (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class booking(models.Model):
    name= models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    seats = models.IntegerField(default=0)
    dia = models.DateField(
        default=timezone.now() + timedelta(days=1)
    )

    def __str__(self):#merknfkenfnek
        return self.name