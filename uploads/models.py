from __future__ import unicode_literals
from django.db import models

# Create your models here.
class upload(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField(null=True, blank=True)
    type=models.CharField(max_length=50)
    file = models.FileField(upload_to='submissions/%Y/%m/%d',)
    school_name=models.CharField(max_length=30)
    class_name=models.IntegerField()
    time=models.DateTimeField('submit_date')
    def __unicode__(self):
        return self.name