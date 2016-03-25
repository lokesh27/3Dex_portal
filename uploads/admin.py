from django.contrib import admin
from .models import upload
# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display=('file','name','description')
    search_fields = ['name','description']
admin.site.register(upload,UploadAdmin)