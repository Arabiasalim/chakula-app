from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Reservation(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.IntegerField()
    description = models.CharField(max_length= 200)
