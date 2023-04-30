from django.db import models
from django.utils import timezone



class DownloadedFile(models.Model):
    user =user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='In progress')

    content = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name
