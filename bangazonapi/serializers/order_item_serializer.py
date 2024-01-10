from rest_framework import serializers
from bangazonapi.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
  """JSON serializer for all orders"""
  class Meta:
    model = OrderItem
    fields = ('id', 'order', 'menu_item')
    depth = 1
