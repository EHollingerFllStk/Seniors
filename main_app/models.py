from django.db import models

# Create your models here.
class Agencies(models.Model):
  def __init__(self, name, address, phone, rating):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    phone = models.CharField(max_length=100)
    rating = models.IntegerField()