# Generated by Django 4.2.11 on 2024-04-05 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_rename_badge_descriptinon_badge_badge_description_and_more'),
        ('post', '0022_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_comments', to='user.profile'),
        ),
    ]
