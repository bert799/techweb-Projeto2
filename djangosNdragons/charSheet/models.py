from django.db import models

# Create your models here.
class Race (models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    desc = models.TextField()
    asi_desc = models.TextField()
    asi = models.TextField() #
    age = models.TextField()
    alignment = models.TextField()
    size = models.TextField()
    speed = models.TextField() #
    speed_desc = models.TextField()
    languages = models.TextField()
    vision = models.TextField()
    traits = models.TextField()
    subraces = models.TextField() #
    document_slug = models.CharField(max_length=40)
    document_title = models.CharField(max_length=40)
    document_license_url = models.CharField(max_length=40)