from django.urls import path
from . import views

urlpatterns = [
    path('Customer/ManageReservation', views.customer_reservation, name="Customer/ManageReservation"),
    path('WaitStaff', views.waitstaff, name="WaitStaff"),
    path('Kitchen', views.kitchen_staff, name="Kitchen"),
    path('KitchenLogin', views.staff_login, {'staff_type': 'kitchen'}, name="KitchenLogin"),
    path('WaitStaffLogin', views.staff_login, {'staff_type': 'waitstaff'}, name="WaitStaffLogin"),
]