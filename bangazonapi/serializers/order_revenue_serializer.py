from rest_framework import serializers
from bangazonapi.models import OrderRevenue

class OrderRevenueSerializer(serializers.ModelSerializer):
  """JSON serializer for order revenue"""
  class Meta:
    model = OrderRevenue
    fields = ('id', 'order', 'order_tip', 'payment_type', 'close_date', 'total_tips', 'payment')
    depth = 1
