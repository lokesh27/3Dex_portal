from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson_name=models.CharField(max_length=20)
    short_description=models.CharField(max_length=50)
    full_description=models.TextField()
    added_date=models.DateTimeField('date added')
    ppt_link=models.TextField()
    def __unicode__(self):
        return self.lesson_name

