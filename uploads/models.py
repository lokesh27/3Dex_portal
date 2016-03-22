from __future__ import unicode_literals

from django.db import models

# Create your models here.
class upload(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(blank=False)
    stlfile = models.FileField(upload_to='stl/%Y/%m/%d',)
    def __unicode__(self):
        return self.name