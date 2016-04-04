from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson_name=models.CharField(max_length=20)
    short_description=models.CharField(max_length=50)
    full_description=models.TextField()
    added_date=models.DateTimeField('date added')
    type=models.CharField(max_length=20,choices=(
    ('VID', 'Video'),
    ('PPT', 'Presentation' ),
    ('PDF', 'Pdf'),
    ))
    SCHOOL_CHOICES = (('abc', 'abc'),('xyz', 'xyz'),('qwe', 'qwe'),)
    CLASS_CHOICES = ((6,6),(7,7),(8,8),(9,9),)
    for_school = MultiSelectField(choices=SCHOOL_CHOICES)
    for_class = MultiSelectField(choices=CLASS_CHOICES)
    link=models.TextField()
    allow=models.BooleanField(default=False)
    def __unicode__(self):
        return self.lesson_name

class MakersBoard(models.Model):
    imgfile=models.ImageField()
    student_name=models.CharField(max_length=30)
    student_class=models.IntegerField()
    student_school=models.CharField(max_length=30)
    show=models.BooleanField(default=False)
    def __unicode__(self):
        return self.student_name