from django.contrib import admin
from django.utils.crypto import get_random_string
from .models import Student
# Register your models here.
def generate_keys(modeladmin, request, queryset):
    queryset.update(secret_key=get_random_string(length=20,allowed_chars=u'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','middle_name','last_name','email_id','phone_no','school_name','secret_key')
    list_filter = ['school_name']
    search_fields = ['first_name','middle_name','last_name','email_id','phone_no','school_name']
    actions = [generate_keys]
generate_keys.short_description = "Generate keys"
admin.site.register(Student,StudentAdmin)