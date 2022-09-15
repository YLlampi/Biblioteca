from django.contrib import admin

# Register your models here.
from .models import Event, Sponsor, File

admin.site.register(File)
admin.site.register(Event)
admin.site.register(Sponsor)
