from django.db import models
from pycountry import pycountry

NATIONALITY_CHOICES = [
    (c.alpha_3, c.name) for c in pycountry.countries
        
]


class Actors(models.Model):
    name = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    nationality  = models.CharField(max_length=3, choices=NATIONALITY_CHOICES, blank=True, null=True)
    


def __str__(self):
    return self.name