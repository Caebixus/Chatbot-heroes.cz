from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 100

admin.site.register(Contact, ContactAdmin)
