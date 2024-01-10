from rest_framework import serializers
from bangazonapi.models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
  """JSON serializer for all menu items"""
  class Meta:
    model = MenuItem
    fields = ('id', 'item_name', 'item_price')
    depth = 0
