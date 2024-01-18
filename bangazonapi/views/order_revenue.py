"""View module for handling revenue requests"""

from django.http import HttpResponseServerError
from django.db.models import Sum
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bangazonapi.models import OrderRevenue, Order, PaymentType, AdminUser, OrderCategory
from bangazonapi.serializers import OrderRevenueSerializer, OrderSerializer


class RevenueView(ViewSet):
  """Order Revenue View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single order revenue"""
    
    try:
      order_revenue = OrderRevenue.objects.get(pk=pk)
      serializer = OrderRevenueSerializer(order_revenue)
      return Response(serializer.data)
    except OrderRevenue.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all order revenues"""
    
    order_revenue = OrderRevenue.objects.all()
    serializer = OrderRevenueSerializer(order_revenue, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    """Handles POST request for order revenue"""
    
    order = Order.objects.get(pk=request.data["order"])
    payment_type = PaymentType.objects.get(pk=request.data["paymentType"])
    
    order_revenue = OrderRevenue.objects.create(
      order = order,
      order_tip = request.data["orderTip"],
      payment_type = payment_type,
    )
    
    order_revenue.save()
    serializer = OrderRevenueSerializer(order_revenue)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  @action(methods=['PATCH'], detail=True)
  def close(self, request, pk=None):
      """decorator to close order"""
      order = Order.objects.get(pk=pk)
      order.is_closed = True
      order.save()
      return Response({'status': 'order closed'}, status=status.HTTP_200_OK)
