# Generated by Django 2.2.6 on 2021-09-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditoriaLead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('lastname', models.CharField(blank=True, max_length=120, null=True)),
                ('company', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('company_size', models.CharField(blank=True, max_length=120, null=True)),
                ('role', models.CharField(blank=True, max_length=120, null=True)),
                ('results', models.CharField(blank=True, max_length=500, null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
