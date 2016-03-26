from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,blank=True)
    email_id=models.EmailField()
    phone_no=models.CharField(max_length=11,blank=True)
    school_name=models.CharField(max_length=30,choices=(('abc','abc'),('xyz','xyz'),('qwe','qwe')))
    class_name=models.IntegerField(choices=((6, 6),(7, 7),(8, 8),(9, 9),))
    avatar=models.ImageField(upload_to="profile_pictures",blank=True)
    def __unicode__(self):
        return self.first_name
