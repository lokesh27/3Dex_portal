from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    uploader = models.CharField(max_length=20,null=True)

    def __unicode__(self):
        return self.question_text

class Reply(models.Model):
    question = models.ForeignKey(Question)
    reply_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.reply_text
