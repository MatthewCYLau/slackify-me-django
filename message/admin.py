from django.contrib import admin

# Register your models here.

from .models import InputMessage

admin.site.register(InputMessage)