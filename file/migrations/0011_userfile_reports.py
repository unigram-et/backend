# Generated by Django 4.2.11 on 2024-04-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_profile_total_points'),
        ('file', '0010_rename_download_userfile_downloads_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfile',
            name='reports',
            field=models.ManyToManyField(blank=True, to='user.profile'),
        ),
    ]