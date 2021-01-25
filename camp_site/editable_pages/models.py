from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=50, blank=False)
    title_image = models.ImageField(blank=True)
    upcoming_event = models.ForeignKey("core.Event", related_name="upcoming_event", on_delete=models.CASCADE)

class Basic(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=50, blank=False)

class ContactUs(models.Model):
    phone_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)], blank=False)
    email = models.EmailField(max_length=254)

class FAQs(models.Model):
    question = models.CharField(max_length=50, blank=False)
    answer = models.CharField(max_length=50, blank=False)
    

