from __future__ import unicode_literals

from django.db import models
from timezone_field import TimeZoneField

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200,blank=True)
    mail = models.EmailField(max_length=70,blank=True, primary_key=True)
    timezone = TimeZoneField(default='Europe/Paris')
    password = models.CharField(max_length=30)

class Bridge(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Sensor(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bridge = models.ForeignKey(Bridge, on_delete=models.SET_NULL, null=True) 


class Channel(models.Model):
    name = models.CharField(max_length=200)
    API_KEY = models.CharField(max_length=16, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensors = models.ManyToManyField(Sensor)
