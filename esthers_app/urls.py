from django.urls import path
from .views import (
    MenuListView,
    OrderCreateView,
    OrderUpdateView,
    OrderCancelView  # Use Case 4
)

urlpatterns = [
    # Use Case 1: View Menu (API)
    path('menu/', MenuListView.as_view(), name='menu-list'),

    # Use Case 2: Place Order
    path('order/', OrderCreateView.as_view(), name='order-create'),

    # Use Case 3: Modify Order
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),

    # Use Case 4: Cancel Order
    path('order/<int:pk>/cancel/', OrderCancelView.as_view(), name='order-cancel'),
]