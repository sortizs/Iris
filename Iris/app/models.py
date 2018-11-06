"""
Definition of models.
"""

from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=254)
    age = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + self.lastname