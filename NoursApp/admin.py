from django.contrib import admin
from .models import Table, Reservation, Dish, Order

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Dish)
admin.site.register(Order)
