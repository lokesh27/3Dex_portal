from django.contrib import admin
from models import upload_dropdown
# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display=('choice_text','for_school','for_class','show')
    list_filter = ['show']
    search_fields = ['choice_text']

admin.site.register(upload_dropdown,UploadAdmin)
