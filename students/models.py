from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,blank=True)
    email_id=models.CharField(max_length=40)
    phone_no=models.CharField(max_length=10)
    school_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20,blank=True)
    def __unicode__(self):
        return self.first_name
