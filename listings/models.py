from turtle import title
from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    num_rooms = models.IntegerField()
    num_beds = models.IntegerField()
    square_foot = models.IntegerField()
    address = models.CharField(max_length=200)
    #image


    def __str__(self):
        return self.title