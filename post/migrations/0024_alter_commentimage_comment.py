# Generated by Django 4.2.11 on 2024-04-05 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_alter_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentimage',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_images', to='post.comment'),
        ),
    ]
