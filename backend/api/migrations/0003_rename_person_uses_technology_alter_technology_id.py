# Generated by Django 5.1.1 on 2024-11-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_project_description_technology_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uses',
            old_name='person',
            new_name='Technology',
        ),
        migrations.AlterField(
            model_name='technology',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
