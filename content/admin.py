from django.contrib import admin
from .models import Lesson,MakersBoard
# Register your models here.
class LessonAdmin(admin.ModelAdmin):
    list_display=('lesson_name','short_description','full_description','added_date','type','link','for_school','for_class','allow')
    list_filter = ['added_date','allow','type']
    search_fields = ['lesson_name','short_description','full_description']

class MakersAdmin(admin.ModelAdmin):
    list_display = ('student_name','imgfile','student_school','student_class','show')
    list_filter = ['show','student_class','student_school']
    search_fields = ['student_name','student_school','student_class']
admin.site.register(Lesson,LessonAdmin)
admin.site.register(MakersBoard,MakersAdmin)