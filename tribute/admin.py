from django.contrib import admin

from .models import TributeMessage

@admin.register(TributeMessage)
class TributeMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'text']
# admin.site.register(TributeMessage)

# Register your models here.
