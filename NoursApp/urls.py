from django.urls import path

from . import views

urlpatterns = [

    path('Customer/ManageReservation', views.customer, name="Customer/ManageReservation"),
    path('WaitStaff', views.waitstaff, name="WaitStaff"),
]
