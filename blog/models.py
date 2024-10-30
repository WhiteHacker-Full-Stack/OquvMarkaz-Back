from telnetlib import CHARSET

from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Pupil(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    fatherName = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    fani = models.ForeignKey('Fan',on_delete=models.CASCADE)
    birth = models.DateField()

    def __str__(self):
        return self.name + " " + self.surname


class Fan(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
    room = models.ForeignKey('Room',on_delete=models.CASCADE)
    lesson_time = models.TimeField()
    juftmi = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    pupilNumber = models.IntegerField(default=0)
    oyligi = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    foiz = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Room(models.Model):
    name=  models.CharField(max_length=50)

    def __str__(self):
        return self.name




