from django.contrib import admin
from .models import Lesson
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display=('lesson_name','short_description','full_description','added_date','type','link','allow','pdf')
    list_filter = ['added_date','allow','type']
    search_fields = ['lesson_name','short_description','full_description']
admin.site.register(Lesson,LessonAdmin)