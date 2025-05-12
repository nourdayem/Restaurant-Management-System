from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer

# Use Case 1: View Menu Items
class MenuListView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Use Case 2: Place Order
class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Use Case 3: Modify Order
class OrderUpdateView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def patch(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status in ['preparing', 'ready', 'completed']:
            return Response(
                {"error": "Cannot modify order once preparation has started."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return self.partial_update(request, *args, **kwargs)

class OrderCancelView(APIView):
    def post(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        if order.status in ['preparing', 'ready', 'completed']:
            return Response(
                {"error": "Cannot cancel an order that is already being processed or completed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = 'cancelled'
        order.save()
        return Response({"message": f"Order {pk} cancelled successfully."}, status=status.HTTP_200_OK)
    
