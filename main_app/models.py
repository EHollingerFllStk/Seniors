from django.db import models


class Agencies(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    phone = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

