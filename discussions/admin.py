from django.contrib import admin
from discussions.models import Question,Reply
# Register your models here.

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]
    list_display = ['question_text', 'pub_date', 'uploader','additional_info','for_school','for_class','show']
    list_filter = ['pub_date', 'uploader','for_school','for_class','show']
    search_fields = ['question_text', 'uploader']


admin.site.register(Question, QuestionAdmin)
