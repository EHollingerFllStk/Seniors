from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SERVICES = (
    ('B', 'Bathing'),
    ('C', 'Cleaning'),
    ('E', 'Errands'),
    ('G', 'Grocery Shopping'),
    ('K', 'Cooking'),
    ('M', 'Companion Care'),
    ('R', 'Reading'),
    ('S', 'Supervising'),
    ('T', 'Toileting'),   
)

class Agencies(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    phone = models.CharField(max_length=100)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'agency_id': self.id})


class Adds(models.Model):
    date = models.DateField('service date')
    service = models.CharField(
        max_length=1,
        choices=SERVICES,
        default=SERVICES[0][0]
    )

    agency = models.ForeignKey(Agencies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']