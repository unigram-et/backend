# Generated by Django 4.2.11 on 2024-04-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_hashtag_slug_remove_hashtag_subscribers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='student_email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
