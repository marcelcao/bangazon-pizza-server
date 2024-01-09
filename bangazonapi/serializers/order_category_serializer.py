from rest_framework import serializers
from bangazonapi.models import OrderCategory

class OrderCategorySerializer(serializers.ModelSerializer):
  """JSON serializer for all order categories"""
  class Meta:
    model = OrderCategory
    fields = ('id', 'category',)
    depth = 0
