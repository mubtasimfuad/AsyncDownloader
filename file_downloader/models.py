from django.db import models
from django.utils import timezone

class File(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)

class Download(models.Model):
    user =user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='in progress')

    def __str__(self):
        return f'{self.file} downloaded by {self.user.username} at {self.downloaded_at}'

