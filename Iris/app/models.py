"""
Definition of models.
"""

from django.db import models

class Participant(models.Model):
    name = models.CharField(max_lenght=254)
    lastname = models.CharField(max_lenght=254)
    email = models.EmailField(max_lenght=254)
    phone = models.CharField(max_lenght=254)
    age = models.IntegerField(max_lenght=2)