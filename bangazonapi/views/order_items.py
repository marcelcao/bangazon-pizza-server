"""View module for handling order item requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import OrderItem
from bangazonapi.serializers import OrderItemSerializer

class OrderItemView(ViewSet):
  """Order Item View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single order item"""
    
    try:
      order_item = OrderItem.objects.get(pk=pk)
      serializer = OrderItemSerializer(order_item)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all order items"""
    
    order_item = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_item, many=True)
    return Response(serializer.data)
