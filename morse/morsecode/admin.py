from django.contrib import admin

# Register your models here.

from .models import Message, Letter

admin.site.register(Message)
admin.site.register(Letter)
