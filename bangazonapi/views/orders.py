"""View module for handling order requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bangazonapi.models import Order, OrderItem, AdminUser, MenuItem
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
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)
  
  @action(methods=['get'], detail=True)
  def items(self, request, pk):
    """Method to get all the items associated to a single order"""
    items = OrderItem.objects.all()
    associated_order = items.filter(order_id=pk)
    
    serializer = OrderItemSerializer(associated_order, many=True)
    return Response(serializer.data)
  
  @action(methods=['delete'], detail=True)
  def remove(self, request, pk):
    """Method to delete items associted to a single order"""
    admin_user = AdminUser.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    orders = Order.objects.all()
    associated_user_order = orders.filter(admin_user=admin_user)
    
    item = MenuItem.objects.get(pk=pk)
    
    order_item = OrderItem.objects.get(
      order = associated_user_order,
      menu_item = item
    )
    order_item.delete()
    return Response({'message': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
  
  @action(methods=['post'], detail=True)
  def add(self, request, pk):
    """Method to add items associted to a single order"""
    admin_user = AdminUser.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
    orders = Order.objects.all()
    associated_user_order = orders.filter(admin_user=admin_user)
    
    item = MenuItem.objects.get(pk=pk)
    
    order_item = OrderItem.objects.create(
      order = associated_user_order,
      menu_item = item
    )
    return Response({'message': 'Item removed'}, status=status.HTTP_204_NO_CONTENT)
    