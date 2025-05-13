# HarisApp/urls.py

from django.urls import path
from . import views



urlpatterns = [

    path('', views.home, name='home'),  # ✅ This must be the first one!
    
    path('payment/<int:order_id>/', views.process_payment, name='process_payment'),
    
    path('payment/success/<int:payment_id>/', views.payment_success, name='payment_success'),
    
    path('staff/', views.staff_list, name='staff_list'),
    
    path('staff/add/', views.add_staff, name='add_staff'),
    
    path('orders/', views.order_list, name='order_list'),
]