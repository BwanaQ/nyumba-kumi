# Generated by Django 3.2 on 2021-04-13 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nyumbax', '0008_auto_20210412_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hood',
            old_name='name',
            new_name='title',
        ),
    ]