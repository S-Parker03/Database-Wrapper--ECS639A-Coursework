# Generated by Django 5.1.1 on 2024-11-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_project_id_alter_uses_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='technology',
            name='description',
            field=models.TextField(),
        ),
    ]