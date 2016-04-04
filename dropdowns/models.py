from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models

# Create your models here.
class upload_dropdown(models.Model):
    choice_text=models.CharField(max_length=30)
    SCHOOL_CHOICES = (('abc', 'abc'),('xyz', 'xyz'),('qwe', 'qwe'),)
    CLASS_CHOICES = ((6,6),(7,7),(8,8),(9,9),)
    for_school = MultiSelectField(choices=SCHOOL_CHOICES)
    for_class = MultiSelectField(choices=CLASS_CHOICES)
    show=models.BooleanField(default=False)

    def __unicode__(self):
        return self.choice_text