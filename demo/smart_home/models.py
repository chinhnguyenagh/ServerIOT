from enum import auto
from typing import no_type_check
from django.db import models
from django.db.models.base import Model  
from django.contrib.auth.models import User
# Create your models
class Home(models.Model):
    """Model definition for House."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for House."""

        verbose_name = 'Home'
        verbose_name_plural = 'Homes'
    name = models.CharField(null = True, blank =False, max_length=50, unique=True)
    temperature = models.IntegerField(default = 25, null = True, blank=True)
    humid = models.IntegerField(null=True, blank=True)
    distance_door = models.IntegerField(null=True,blank=True)
    distance_private_room = models.IntegerField(null=True, blank=True)
    host_mqtt = models.CharField(null=True, blank=True,max_length=100)
    port_mqtt = models.CharField(null=True, blank=True, max_length=10)
    topic = models.CharField(null=True, blank=True,max_length=100)



    def __str__(self):
        """Unicode representation of House."""
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, null=False,blank=False, unique=True)

    def __str__(self):
        return self.name

class Devide(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False)
    type = models.ForeignKey('smart_home.Type', on_delete=models.CASCADE, null=False,blank=False)
    status = models.BooleanField(default=False, null=True, blank=True)
    auto = models.BooleanField(default=True,null=True,blank=True)
    house = models.ForeignKey('smart_home.Home', on_delete=models.CASCADE, null=True, blank=True)
    pin_number = models.IntegerField(unique=True, null=True, blank=True)
    max_value = models.FloatField(null=True, blank=True)
    min_value = models.FloatField(null=True, blank=True)