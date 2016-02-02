from django.contrib import admin
from .models import Feed
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name','email_id','query')
    search_fields = ['email_id','name','query']
admin.site.register(Feed,FeedbackAdmin)