from django.contrib import admin
from main.models.business import Business

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'description', 'website', )
