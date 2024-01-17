"""View module for handling order requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bangazonapi.models import Order, OrderItem, AdminUser, OrderCategory, OrderRevenue
from bangazonapi.serializers import OrderSerializer, OrderItemSerializer
class OrderView(ViewSet):
  """Order View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single order"""
    
    try:
      order = Order.objects.get(pk=pk)
      serializer = OrderSerializer(order)
      return Response(serializer.data)
    except Order.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all orders"""
    
    order = Order.objects.all()
    admin_user = AdminUser.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    associated_user = order.filter(admin_user=admin_user)
    serializer = OrderSerializer(associated_user, many=True)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE request for order"""
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def create(self, request):
    """Handles POST request for order"""
    
    admin_user = AdminUser.objects.get(uid=request.data["adminUser"])
    order_type = OrderCategory.objects.get(pk=request.data["orderType"])
    is_closed = False
    
    order = Order.objects.create(
      admin_user = admin_user,
      order_name = request.data["orderName"],
      customer_phone = request.data["customerPhone"],
      customer_email = request.data["customerEmail"],
      order_type = order_type,
      is_closed = is_closed,
    )
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT request for order"""
    
    order = Order.objects.get(pk=pk)
    order.order_name = request.data["orderName"]
    order.customer_phone = request.data["customerPhone"]
    order.customer_email = request.data["customerEmail"]
    
    admin_user = AdminUser.objects.get(uid=request.data["adminUser"])
    order.admin_user = admin_user
    
    order_type = OrderCategory.objects.get(pk=request.data["orderType"])
    order.order_type = order_type
    
    is_closed = False
    order.is_closed = is_closed
    
    order.save()
    serializer = OrderSerializer(order)
    return Response (serializer.data, status=status.HTTP_200_OK)

  @action(methods=['get'], detail=True)
  def items(self, request, pk):
    """Method to get all the items associated to a single order"""
    items = OrderItem.objects.all()
    associated_order = items.filter(order_id=pk)
    
    serializer = OrderItemSerializer(associated_order, many=True)
    return Response(serializer.data)
  
