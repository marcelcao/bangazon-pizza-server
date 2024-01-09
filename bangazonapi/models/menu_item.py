from django.db import models

class MenuItem(models.Model):

    item_name = models.CharField(max_length=50)
    item_price = models.FloatField()
