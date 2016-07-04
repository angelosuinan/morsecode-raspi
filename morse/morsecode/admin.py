from django.contrib import admin

# Register your models here.

from .models import Message, Letters

admin.site.register(Message)
admin.site.register(Letters)
