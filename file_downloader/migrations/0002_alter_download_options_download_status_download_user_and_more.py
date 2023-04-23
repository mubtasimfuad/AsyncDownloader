# Generated by Django 4.2 on 2023-04-23 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file_downloader', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='download',
            options={},
        ),
        migrations.AddField(
            model_name='download',
            name='status',
            field=models.CharField(default='in progress', max_length=20),
        ),
        migrations.AddField(
            model_name='download',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='download',
            name='downloaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='download',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_downloader.file'),
        ),
    ]
