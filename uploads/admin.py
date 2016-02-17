from django.contrib import admin
from .models import upload
# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display=('stlfile','name')
    search_fields = ['name']
admin.site.register(upload,UploadAdmin)