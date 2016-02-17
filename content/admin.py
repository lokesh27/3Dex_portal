from django.contrib import admin
from .models import Lesson
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display=('lesson_name','short_description','full_description','added_date','ppt_link')
    list_filter = ['added_date']
    search_fields = ['lesson_name','short_description','full_description']
admin.site.register(Lesson,LessonAdmin)