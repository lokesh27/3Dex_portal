from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Feed(models.Model):
    name=models.CharField(max_length=30)
    email_id=models.EmailField()
    query=models.TextField()
    def __unicode__(self):
        return self.name