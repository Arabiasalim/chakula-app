from django.db import models

class message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=200)


class Reservation(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    num_people = models.IntegerField()
    description = models.CharField(max_length= 200)
