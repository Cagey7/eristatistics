# Generated by Django 4.2.6 on 2023-12-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('macrobulletin', '0002_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='path',
        ),
        migrations.AddField(
            model_name='table',
            name='excel',
            field=models.FileField(blank=True, default=None, null=True, upload_to='excels'),
        ),
    ]
