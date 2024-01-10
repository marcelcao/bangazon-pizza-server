from rest_framework import serializers
from bangazonapi.models import PaymentType

class PaymentTypeSerializer(serializers.ModelSerializer):
  """JSON serializer for all payment type options"""
  class Meta:
    model = PaymentType
    fields = ('id', 'type')
    depth = 0
