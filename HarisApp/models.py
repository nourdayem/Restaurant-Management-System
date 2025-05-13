# HarisApp/models.py

from django.db import models

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('CASH', 'Cash'),
        ('CARD', 'Credit/Debit Card'),
        ('ONLINE', 'Online Payment'),
    ]
    
    order = models.ForeignKey('Order', on_delete=models.CASCADE)  # ForeignKey to your Order model
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField(default=False)  # True if paid, False if pending
    payment_date = models.DateTimeField(auto_now_add=True)  # When payment was made

    def __str__(self):
        return f"Payment for Order {self.order.id} - {'Paid' if self.payment_status else 'Pending'}"
    

    # HarisApp/models.py

class Staff(models.Model):
    ROLE_CHOICES = [
        ('CHEF', 'Chef'),
        ('WAITER', 'Waiter'),
        ('MANAGER', 'Manager'),
        ('CLEANER', 'Cleaner'),
    ]
    
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hire_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_role_display()}"


# HarisApp/models.py

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=255)
    items = models.TextField()  # List of ordered items (could be JSON or string)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.customer_name} - {self.get_status_display()}"
