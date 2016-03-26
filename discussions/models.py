from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    uploader = models.CharField(max_length=30)
    additional_info=models.TextField(null=True,blank=True)
    for_class=models.IntegerField(choices=((6, 6),(7, 7),(8, 8),(9, 9),))
    for_school=models.CharField(max_length=30,choices=(('abc','abc'),('xyz','xyz'),('qwe','qwe')))
    show=models.BooleanField(default=False)
    def __unicode__(self):
        return self.question_text

class Reply(models.Model):
    question = models.ForeignKey(Question)
    reply_text = models.CharField(max_length=200)
    name=models.CharField(max_length=30)
    def __unicode__(self):
        return self.reply_text
