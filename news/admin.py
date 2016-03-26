from django.contrib import admin
from models import News
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_heading','news_text','for_class','for_school','news_date','show']
    search_fields = ['news_heading','news_text']
    list_filter = ['news_date','for_class','for_school','show']
admin.site.register(News,NewsAdmin)