from django.contrib import admin
from main.models import Customer, Employee, ItemOrderLink, Menu, Item, Order, Venue

#class VenueAdmin(admin.ModelAdmin):
#    list_display = ('id', 'name', 'address', 'description', 'website', )

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(ItemOrderLink)
admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Venue)