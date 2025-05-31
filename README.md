Restaurant Management System
A Django web application for managing restaurant reservations and staff operations.
Features

Customer Reservations: Book and manage table reservations with confirmation codes
Kitchen Dashboard: View and prepare orders
Waitstaff Dashboard: Serve orders and track completion
Admin Panel: Full system management

Demo Credentials
RoleUsernamePasswordKitchen Staffkitchen_staff1kitchenpass123Waitstaffwait_staff1wait_staff1AdminadminRAcEVkB6T8
Quick Start

Clone the repository:
bashgit clone https://github.com/nourdayem/Restaurant-Management-System.git
cd Restaurant-Management-System

Install Django and run:
bashpip install django
python manage.py migrate
python manage.py runserver

Visit: http://127.0.0.1:8000/
Test with the demo credentials above

How to Use
Customers

Go to homepage → "Book a Table"
Use confirmation code to manage reservations

Kitchen Staff

Login at /KitchenLogin
View pending orders and mark as ready

Waitstaff

Login at /WaitStaffLogin
Serve ready orders to customers

Admin

Access /admin/ for full system control

Technology

Django 4.2
SQLite Database
HTML/CSS/JavaScript
Responsive Design

Author
Nour Dayem - @nourdayem
