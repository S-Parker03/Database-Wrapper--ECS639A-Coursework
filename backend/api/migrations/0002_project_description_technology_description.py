# Generated by Django 5.1.1 on 2024-11-07 16:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technology',
            name='description',
            field=models.CharField(default=2, max_length=256),
            preserve_default=False,
        ),
    ]