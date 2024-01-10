"""View module for handling order requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import Order
from bangazonapi.serializers import OrderSerializer

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
