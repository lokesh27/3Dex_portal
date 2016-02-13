from django.contrib import admin
from .models import Lesson
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display=('lesson_name','lesson_description','added_date','ppt_link')
    list_filter = ['added_date']
    search_fields = ['lesson_name','lesson_description']
admin.site.register(Lesson,LessonAdmin)