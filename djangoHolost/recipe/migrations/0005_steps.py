# Generated by Django 5.1.1 on 2024-09-28 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_alter_posts_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_des', models.TextField(max_length=1000)),
                ('step_image', models.ImageField(blank=True, null=True, upload_to='step_pics')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipe.posts')),
            ],
        ),
    ]
