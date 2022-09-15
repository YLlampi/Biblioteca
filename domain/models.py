from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    site = models.CharField(max_length=50)
    link = models.URLField(max_length=255, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_event = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-date_created', '-date_event']

    def __str__(self):
        return f'{self.name}'


class File(models.Model):
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=15)
    description = models.TextField(max_length=255, null=True, blank=True)
    link_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    pdf_file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    autor_file = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nro_downloads = models.PositiveBigIntegerField

    def __str__(self):
        return f'{self.title}'


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    link_company = models.URLField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
