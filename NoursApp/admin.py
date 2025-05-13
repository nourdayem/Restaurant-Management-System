from django.contrib import admin
from .models import Customer, Staff, Table, Reservation, Order, FoodItem

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(FoodItem)