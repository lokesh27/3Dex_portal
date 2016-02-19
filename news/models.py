from __future__ import unicode_literals

from django.db import models

# Create your models here.
class News(models.Model):
    news_heading=models.CharField(max_length=50)
    news_text=models.TextField()
    news_date=models.DateTimeField()
    def __unicode__(self):
        return self.news_heading