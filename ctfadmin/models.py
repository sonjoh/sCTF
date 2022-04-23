from django.db import models
from django.urls.resolvers import LocaleRegexDescriptor

# Create your models here.

class Settings(models.Model):
    ctf_name            = models.CharField(max_length=60)
    ctf_active          = models.BooleanField(default=True)
    uploaded_logo       = models.BooleanField(default=False)
    logo_link           = models.CharField(max_length=255, default="")
    uploaded_favicon    = models.BooleanField(default=False)
    favicon_link        = models.CharField(max_length=255, default="")