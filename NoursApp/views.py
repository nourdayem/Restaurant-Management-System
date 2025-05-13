from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer, Staff, Table, Reservation, Order, FoodItem
from django.utils import timezone
import random
import string
from django.contrib.auth import authenticate, login

# Function to generate a random confirmation code
def generate_confirmation_code(length=8):
    """Generate a random alphanumeric confirmation code"""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# UC5: Manage Reservations (Customer-focused)
def customer_reservation(request):
    """
    View for customers to manage their reservations.
    Allows customers to create, view, and modify their reservations.
    """
    if request.method == 'POST':
        # Check if action for existing reservation
        if 'action' in request.POST and 'reservation_id' in request.POST:
            reservation_id = request.POST.get('reservation_id')
            action = request.POST.get('action')
            
            # Handle confirmation code verification
            confirmation_code = request.POST.get('confirmation_code')
            reservation = get_object_or_404(Reservation, id=reservation_id)
            
            # Verify the confirmation code
            if reservation.confirmation_code != confirmation_code:
                messages.error(request, 'Invalid confirmation code. Please try again.')
                return redirect('Customer/ManageReservation')
            
            if action == 'confirm':
                reservation.status = 'Confirmed'
                reservation.save()
                messages.success(request, f'Reservation confirmed!')
            elif action == 'cancel':
                reservation.status = 'Cancelled'
                reservation.save()
                messages.success(request, f'Reservation cancelled!')
            elif action == 'update':
                # Handle update action with confirmation code
                new_date = request.POST.get('new_date')
                new_time = request.POST.get('new_time')
                new_guests = request.POST.get('new_guests')
                
                if all([new_date, new_time, new_guests]):
                    reservation.date = new_date
                    reservation.time = new_time
                    reservation.guests = int(new_guests)
                    reservation.save()
                    messages.success(request, 'Reservation updated successfully!')
                else:
                    messages.error(request, 'Please fill in all fields for the update.')
            
            return redirect('Customer/ManageReservation')
        
        # Process new reservation
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        
        # Create or get customer
        customer, created = Customer.objects.get_or_create(
            name=name,
            defaults={'contact_info': contact_info}
        )
        if not created and contact_info:
            customer.contact_info = contact_info
            customer.save()
        
        # Create reservation
        if all([date, time, guests]):
            # Check table availability
            existing_reservations = Reservation.objects.filter(
                date=date,
                time=time,
                status='Confirmed'
            )
            
            available_tables = Table.objects.filter(capacity__gte=int(guests))
            
            # Crude check - in a real system, you'd have more sophisticated availability logic
            if available_tables.exists():
                # Generate confirmation code
                confirmation_code = generate_confirmation_code()
                
                reservation = Reservation(
                    customer=customer,
                    date=date,
                    time=time,
                    guests=int(guests),
                    status='Pending',
                    confirmation_code=confirmation_code
                )
                reservation.save()
                messages.success(request, f'Reservation created successfully! Your confirmation code is: {confirmation_code}. Please keep this code to manage your reservation.')
            else:
                messages.error(request, 'Sorry, no tables available for that date and time with your party size.')
            
            return redirect('Customer/ManageReservation')
    
    # Check if we're managing with confirmation code
    if 'find_reservation' in request.GET:
        confirmation_code = request.GET.get('confirmation_code', '')
        if confirmation_code:
            reservations = Reservation.objects.filter(confirmation_code=confirmation_code)
            if reservations.exists():
                return render(request, 'NoursApp/manage_reservation.html', {
                    'reservations': reservations,
                    'found': True,
                    'confirmation_code': confirmation_code
                })
            else:
                messages.error(request, 'No reservation found with that confirmation code.')
    
    # Get all tables and reservations for reference
    tables = Table.objects.all()
    
    return render(request, 'NoursApp/manage_reservation.html', {
        'tables': tables
    })

# UC6: Serve Food (Waitstaff)

@login_required(login_url='/WaitStaffLogin')
def waitstaff(request):
    """
    View for waitstaff to manage food service.
    Allows wait staff to see orders ready for serving and mark them as served.
    """
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')
        
        if order_id and action:
            order = get_object_or_404(Order, id=order_id)
            
            if action == 'mark_served':
                order.status = 'Served'
                order.save()
                messages.success(request, f'Order #{order.id} has been marked as served to the customer')
            
            elif action == 'log_issue':
                issue_description = request.POST.get('issue_description')
                if issue_description:
                    # In a real system, you'd log this to a table or notification system
                    # For now, we'll just use a message
                    messages.warning(request, f'Issue logged for Order #{order.id}: {issue_description}')
                else:
                    messages.error(request, 'Please provide a description of the issue')
    
    # Get orders that are ready to be served
    ready_orders = Order.objects.filter(status='Ready')
    # Get all active orders for reference
    all_active_orders = Order.objects.exclude(status='Served')
    # Recent served orders (for verification)
    recently_served = Order.objects.filter(status='Served').order_by('-timestamp')[:5]
    
    context = {
        'ready_orders': ready_orders,
        'all_active_orders': all_active_orders,
        'recently_served': recently_served
    }
    
    return render(request, 'NoursApp/waitstaff.html', context)

# UC7: Prepare Food (Kitchen Staff
@login_required(login_url='/KitchenLogin')
def kitchen_staff(request):
    """
    View for kitchen staff to manage food preparation.
    Allows kitchen staff to see pending orders, start preparation, and mark orders as ready.
    """
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')
        
        if order_id and action:
            order = get_object_or_404(Order, id=order_id)
            
            if action == 'start_preparation':
                order.status = 'Preparing'
                order.save()
                messages.success(request, f'Started preparing order #{order.id}')
            
            elif action == 'mark_ready':
                order.status = 'Ready'
                order.save()
                messages.success(request, f'Order #{order.id} marked as ready for serving')
                
            elif action == 'report_shortage':
                missing_item = request.POST.get('missing_item')
                if missing_item:
                    # In a real system, you'd update inventory and notify management
                    # For now, we'll just use a message
                    messages.warning(request, f'Ingredient shortage reported: {missing_item}')
                else:
                    messages.error(request, 'Please specify which ingredient is missing')
    
    # Get orders that need to be prepared
    pending_orders = Order.objects.filter(status='Pending')
    # Get orders currently being prepared
    preparing_orders = Order.objects.filter(status='Preparing')
    # Get orders that are ready (for verification)
    ready_orders = Order.objects.filter(status='Ready')
    
    context = {
        'pending_orders': pending_orders,
        'preparing_orders': preparing_orders,
        'ready_orders': ready_orders
    }
    
    return render(request, 'NoursApp/kitchen.html', context)

def staff_login(request, staff_type):
    """
    View for staff login - supports both kitchen and waitstaff
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if user has the right role/group
            # You might want to add staff groups in admin panel
            # For now we'll use a simple approach based on username prefix
            if staff_type == 'kitchen':
                if username.startswith('kitchen_'):
                    login(request, user)
                    return redirect('Kitchen')
                else:
                    messages.error(request, 'You do not have kitchen staff privileges.')
            elif staff_type == 'waitstaff':
                if username.startswith('wait_'):
                    login(request, user)
                    return redirect('WaitStaff')
                else:
                    messages.error(request, 'You do not have waitstaff privileges.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'NoursApp/staff_login.html', {'staff_type': staff_type})