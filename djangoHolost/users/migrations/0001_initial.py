# Generated by Django 4.2.7 on 2024-08-02 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('family', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.CharField(max_length=256, verbose_name='E-mail')),
                ('number', models.CharField(max_length=11, verbose_name='Номер телефона')),
            ],
        ),
    ]
