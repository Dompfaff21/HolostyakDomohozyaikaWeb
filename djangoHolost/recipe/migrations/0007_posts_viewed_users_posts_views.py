# Generated by Django 4.2.7 on 2024-11-06 16:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0006_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='viewed_users',
            field=models.ManyToManyField(blank=True, related_name='viewed_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posts',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
