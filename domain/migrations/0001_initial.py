# Generated by Django 4.1 on 2022-08-29 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('site', models.CharField(max_length=50)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_event', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_created', '-date_event'],
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link_company', models.URLField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('pdf_file', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('auto_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('link_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='domain.event')),
            ],
        ),
    ]
