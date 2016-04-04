from django.contrib import admin
from .models import upload
# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display=('file','name','description','type')
    search_fields = ['name','description']
    list_filter = ['type']
admin.site.register(upload,UploadAdmin)