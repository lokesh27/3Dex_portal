from django.contrib import admin
from .models import Vids
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display=('video_description','date','video_link',)
    list_filter = ['date']
    search_fields = ['video_description']
admin.site.register(Vids,VideoAdmin)