from __future__ import unicode_literals

from django.db import models

# Create your models here.
class News(models.Model):
    news_heading=models.CharField(max_length=50)
    news_text=models.TextField()
    news_date=models.DateTimeField()
    for_class=models.IntegerField(choices=((6, 6),(7, 7),(8, 8),(9, 9),))
    for_school=models.CharField(max_length=30,choices=(('abc','abc'),('xyz','xyz'),('qwe','qwe')))
    show=models.BooleanField(default=False)
    def __unicode__(self):
        return self.news_heading