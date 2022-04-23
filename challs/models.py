from django.db import models

# Create your models here.
#https://www.youtube.com/watch?v=IiUYyZo2gTk

class Challs(models.Model):
    name            = models.CharField(max_length=255)
    active          = models.BooleanField(default=True)
    static_value    = models.BooleanField(default=False)
    points          = models.IntegerField(default=1000)
    solves          = models.IntegerField(default=0)
    category        = models.CharField(max_length=255)
    task            = models.CharField(max_length=255)
    flags           = models.CharField(max_length=255, default="")
    casesens        = models.BooleanField(default=True)
    files           = models.CharField(max_length=255, default="")
    time_created    = models.CharField(max_length=255, default="JANUAR 2022")

