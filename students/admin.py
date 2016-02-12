from django.contrib import admin
from django.utils.crypto import get_random_string
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','middle_name','last_name','email_id','phone_no','school_name')
    list_filter = ['school_name']
    search_fields = ['first_name','middle_name','last_name','email_id','phone_no','school_name']
admin.site.register(Student,StudentAdmin)