from django.contrib import admin
from .models import Table, Reservation, dishe, Order

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(dishe)
admin.site.register(Order)
