# Generated by Django 2.2.6 on 2019-10-23 18:45

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20191023_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=courses.models.file_upload_location),
        ),
    ]