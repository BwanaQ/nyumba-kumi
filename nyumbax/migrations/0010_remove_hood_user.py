# Generated by Django 3.2 on 2021-04-13 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyumbax', '0009_rename_name_hood_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hood',
            name='user',
        ),
    ]
