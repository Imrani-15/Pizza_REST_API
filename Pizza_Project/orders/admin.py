from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer','size','order_status','quantity','created_at','update_at']
    list_filter = ['created_at','order_status','size']
admin.site.register(Order,OrderAdmin)