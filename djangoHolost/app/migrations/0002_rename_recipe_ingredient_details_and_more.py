# Generated by Django 4.2.7 on 2024-11-24 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe',
            new_name='Details',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='Ingredients',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='name',
            new_name='Recipe',
        ),
    ]
