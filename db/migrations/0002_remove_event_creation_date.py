# Generated by Django 5.0 on 2023-12-05 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='creation_date',
        ),
    ]
