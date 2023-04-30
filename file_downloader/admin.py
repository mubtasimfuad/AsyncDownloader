from django.contrib import admin
from .models import DownloadedFile

class DownloadedFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)

admin.site.register(DownloadedFile, DownloadedFileAdmin)
