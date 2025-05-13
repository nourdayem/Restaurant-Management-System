# HarisApp/forms.py

from django import forms
from .models import Staff, Payment

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']
