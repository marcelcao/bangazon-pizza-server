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
