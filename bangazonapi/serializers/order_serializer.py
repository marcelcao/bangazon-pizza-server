from rest_framework import serializers
from bangazonapi.models import Order

class OrderSerializer(serializers.ModelSerializer):
  """JSON serializer for all orders"""
  class Meta:
    model = Order
    fields = ('id', 'admin_user', 'order_name', 'customer_phone', 'customer_email', 'order_type', 'is_closed')
    depth = 1
