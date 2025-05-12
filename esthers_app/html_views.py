from django.shortcuts import render
from .models import MenuItem

def menu_template_view(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})