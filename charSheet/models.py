from django.db import models

# Create your models here.
class Character (models.Model):
    name = models.CharField(max_length=40)
    race = models.CharField(max_length=15)
    playerClass = models.CharField(max_length=30)