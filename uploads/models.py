from __future__ import unicode_literals

from django.db import models

# Create your models here.
class upload(models.Model):
    stlfile = models.FileField(upload_to='stl/%Y/%m/%d')