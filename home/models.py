from os import name
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    