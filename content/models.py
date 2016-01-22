from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson_name=models.CharField(max_length=20)
    lesson_description=models.CharField(max_length=50,null=True)
    added_date=models.DateTimeField('date added')
    video_link=models.CharField(max_length=500)
    def __unicode__(self):
        return self.lesson_name

class Assignment(models.Model):
    lesson=models.ForeignKey(Lesson)
    notes=models.TextField(blank=True)
