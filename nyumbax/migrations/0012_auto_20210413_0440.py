# Generated by Django 3.2 on 2021-04-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nyumbax', '0011_alter_essential_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='essential',
            old_name='location',
            new_name='hood',
        ),
        migrations.AlterField(
            model_name='hood',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]