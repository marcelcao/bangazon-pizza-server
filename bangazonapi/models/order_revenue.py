from django.db import models
from django.db.models import Count, Sum
from .order import Order
from .payment_type import PaymentType
class OrderRevenue(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="total_revenue")
    order_tip = models.FloatField()
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    close_date = models.DateField(auto_now=True)

    @property
    def total_tips(self):
      tips = OrderRevenue.objects.aggregate(tip_total=Sum('order_tip')) ['tip_total']
      return tips
    
    @property
    def payment(self):
        payment_type_id = self.payment_type.id
        return OrderRevenue.objects.filter(payment_type__id=payment_type_id).count()
      
    @property
    def total_values(self):
        """Sum of menu items"""
        order_instance = getattr(self, 'order', None)
        if order_instance is not None:
            return order_instance.custom_total_values
        return 0
    
    @property
    def order_category(self):
        order_instance = getattr(self, 'order', None)
        
        if order_instance:
            order_type_id = order_instance.order_type.id
            return OrderRevenue.objects.filter(order__order_type__id=order_type_id).count()
        
        return 0
    
      
