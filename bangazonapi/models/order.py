from django.db import models
from .admin_user import AdminUser
from .order_category import OrderCategory

class Order(models.Model):

    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE, related_name="orders")
    order_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=50)
    order_type = models.ForeignKey(OrderCategory, on_delete=models.CASCADE)
    is_closed = models.BooleanField()
    
    @property
    def total_order(self):
        """Sum of menu items"""
        order_items = getattr(self, 'order_items', None)
        if order_items is not None:
            return sum([order_item.menu_item.item_price for order_item in order_items.all()])
        return 0
