from django.contrib import admin
from apps.second.models import Contact

# Register your models here.
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ["title","description"]
    search_fields = ["title"]
