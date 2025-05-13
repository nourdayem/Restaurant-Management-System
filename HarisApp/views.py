# HarisApp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff, Payment, Order
from .forms import StaffForm, PaymentForm  # if using forms
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'HarisApp/staff_list.html', {'staff': staff_members})

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'HarisApp/add_staff.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'HarisApp/order_list.html', {'orders': orders})

def process_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.payment_status = True
            payment.save()
            return redirect('payment_success', payment_id=payment.id)
    else:
        form = PaymentForm()
    return render(request, 'HarisApp/process_payment.html', {'form': form, 'order': order})

def payment_success(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'HarisApp/payment_success.html', {'payment': payment})
