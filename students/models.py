from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,blank=True)
    email_id=models.EmailField()
    phone_no=models.CharField(max_length=11)
    school_name=models.CharField(max_length=50)
    class_name=models.CharField(max_length=10)
    def __unicode__(self):
        return self.first_name
