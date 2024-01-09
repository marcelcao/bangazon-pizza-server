from django.db import models
from .order import Order
from .menu_item import MenuItem

class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
