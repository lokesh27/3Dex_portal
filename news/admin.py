from django.contrib import admin
from models import News
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_heading','news_text']
    search_fields = ['news_heading','news_text']
    list_filter = ['news_date']
admin.site.register(News,NewsAdmin)