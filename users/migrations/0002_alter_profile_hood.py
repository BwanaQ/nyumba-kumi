# Generated by Django 3.2 on 2021-04-12 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nyumbax', '0007_post_hood'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hood',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='nyumbax.hood'),
        ),
    ]