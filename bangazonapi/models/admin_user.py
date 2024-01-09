from django.db import models

class AdminUser(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
