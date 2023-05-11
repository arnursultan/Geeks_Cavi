from django.contrib import admin
from apps.geeks.models import Geeks

# Register your models here.
@admin.register(Geeks)
class GeeksAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_filter = ['title']
    search_fields = ['title']