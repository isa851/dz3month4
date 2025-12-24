from django.contrib import admin
from apps.base.models import Settings

# Register your models here.
@admin.register(Settings)
class Settings(admin.ModelAdmin):
    list_display = ["title","description"]
    search_fields = ["title"]
    # readonly_fields = ["description"]