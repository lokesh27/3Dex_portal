from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vids(models.Model):
    video_description=models.CharField(max_length=50)
    date=models.DateTimeField('date')
    video_link=models.TextField()
    def __unicode__(self):
        return self.video_description

