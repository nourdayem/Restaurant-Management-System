from django.db import models
from django.contrib.auth.models import User

# Customer model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Staff model
class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} ({self.role})"

# Table model
class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"

# Reservation model
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    confirmation_code = models.CharField(max_length=8, unique=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.customer.name} - {self.date} {self.time}"

# Order model
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Served', 'Served'),
    ]
    
    table_number = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    allergy_info = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} - Table {self.table_number} - {self.status}"

# FoodItem model
class FoodItem(models.Model):
    order = models.ForeignKey(Order, related_name='food_items', on_delete=models.CASCADE)
    dish_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    special_instructions = models.TextField(blank=True)
    dietary_restrictions = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.dish_name} (x{self.quantity})"