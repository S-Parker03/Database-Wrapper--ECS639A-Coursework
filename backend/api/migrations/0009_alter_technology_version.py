# Generated by Django 5.1.1 on 2024-11-08 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_project_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='version',
            field=models.IntegerField(),
        ),
    ]