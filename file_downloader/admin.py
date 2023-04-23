from django.contrib import admin
from .models import File,Download

class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'url')

admin.site.register(File, FileAdmin)

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_filter = ('downloaded_at',)
    search_fields = ('file_name',)
