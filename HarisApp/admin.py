# HarisApp/admin.py

from django.contrib import admin
from .models import Payment, Staff, Order

admin.site.register(Payment)
admin.site.register(Staff)
admin.site.register(Order)
