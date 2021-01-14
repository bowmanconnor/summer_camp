from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
from django.core.validators import MaxValueValidator
from datetime import datetime    


# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=1000000, blank=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    end_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)

    address_line_1 = models.CharField(max_length=128, blank=False)
    address_line_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=False)
    state = USStateField(null=False)
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)], blank=False)

    is_open = models.BooleanField(default=True)
    # number_campers = models.IntegerField(blank=True, default=0)
    # campers = models.ForeignKey("core.Camper", related_name="camper", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    

class Gymnast(models.Model):
    GROUP_CHOICES = [
        ('B', 'Boys'), 
        ('G', 'Girls')
    ]
    name = models.CharField(max_length=50, blank=False)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(99)], blank=False)
    group = models.CharField(max_length=1, choices=GROUP_CHOICES, blank=False)
    event = models.ForeignKey('core.Event', related_name='event', on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

class Coach(models.Model):
    name = models.CharField(max_length=50, blank=False)
    bio = models.CharField(max_length=256, blank=False)
    pic = models.ImageField(upload_to='coaches', blank=True)
