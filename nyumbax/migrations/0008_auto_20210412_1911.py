# Generated by Django 3.2 on 2021-04-12 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nyumbax', '0007_post_hood'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='business',
            options={'verbose_name_plural': 'businesses'},
        ),
        migrations.AddField(
            model_name='business',
            name='hood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nyumbax.hood'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hood',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hood',
            name='admin',
            field=models.CharField(max_length=100),
        ),
    ]
