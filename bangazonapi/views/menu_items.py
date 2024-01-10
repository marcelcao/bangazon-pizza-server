"""View module for handling menu item requests"""

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bangazonapi.models import MenuItem
from bangazonapi.serializers import MenuItemSerializer

class MenuItemView(ViewSet):
  """Menu Item View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single menu item"""
    
    try:
      menu_item = MenuItem.objects.get(pk=pk)
      serializer = MenuItemSerializer(menu_item)
      return Response(serializer.data)
    except MenuItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all menu items"""
    
    menu_item = MenuItem.objects.all()
    serializer = MenuItemSerializer(menu_item, many=True)
    return Response(serializer.data)
