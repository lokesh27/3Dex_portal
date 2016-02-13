from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson_name=models.CharField(max_length=20)
    lesson_description=models.TextField(blank=True,null=True)
    added_date=models.DateTimeField('date added')
    ppt_link=models.TextField()
    def __unicode__(self):
        return self.lesson_name

