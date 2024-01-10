"""View module for handling payment type requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import PaymentType
from bangazonapi.serializers import PaymentTypeSerializer

class PaymentTypeView(ViewSet):
  """Payment Type View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single payment type option"""
    
    try:
      payment_type = PaymentType.objects.get(pk=pk)
      serializer = PaymentTypeSerializer(payment_type)
      return Response(serializer.data)
    except PaymentType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all payment type options"""
    
    payment_type = PaymentType.objects.all()
    serializer = PaymentTypeSerializer(payment_type, many=True)
    return Response(serializer.data)
