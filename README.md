# Restaurant Management System

A Django web application for managing restaurant reservations and staff operations.

## Features

- **Customer Reservations**: Book and manage table reservations with confirmation codes
- **Kitchen Dashboard**: View and prepare orders 
- **Waitstaff Dashboard**: Serve orders and track completion
- **Admin Panel**: Full system management

## Demo Credentials

| Role | Username | Password |
|------|----------|----------|
| Kitchen Staff | `kitchen_staff1` | `kitchenpass123` |
| Waitstaff | `wait_staff1` | `waitpass123` |
| Admin | `admin` | `RAcEVkB6T8` |

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/nourdayem/Restaurant-Management-System.git
   cd Restaurant-Management-System
   ```

2. Install Django and run:
   ```bash
   pip install django
   python manage.py migrate
   python manage.py runserver
   ```

3. Visit: `http://127.0.0.1:8000/`

4. Test with the demo credentials above

## How to Use

### Customers
- Go to homepage → "Book a Table"
- Use confirmation code to manage reservations

### Kitchen Staff
- Login at `/KitchenLogin`
- View pending orders and mark as ready

### Waitstaff  
- Login at `/WaitStaffLogin`
- Serve ready orders to customers

### Admin
- Access `/admin/` for full system control

## Technology

- Django 4.2
- SQLite Database
- HTML/CSS/JavaScript
- Responsive Design

## Author

Nour Dayem - [@nourdayem](https://github.com/nourdayem)
