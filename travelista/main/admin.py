from django.contrib import admin
from main.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name', 'created_date')
    list_filter = ['created_date']
    search_fields = ['subject', 'name', 'message']
    ordering = ['-created_date']
