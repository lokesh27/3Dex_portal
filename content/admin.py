from django.contrib import admin
from .models import Lesson,Assignment
# Register your models here.
class AssignmentInline(admin.StackedInline):
    model=Assignment
    extra=1
class LessonAdmin(admin.ModelAdmin):
    list_display=('lesson_name','lesson_description','added_date','video_link')
    list_filter = ['added_date']
    search_fields = ['lesson_name','lesson_description']
    inlines=[AssignmentInline]
admin.site.register(Lesson,LessonAdmin)