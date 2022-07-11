from django.db import models
from datetime import datetime

   

class Products(models.Model):
    name = models.CharField(max_length=40)
    timestamp=models.DateTimeField(auto_now_add=True)
    warehouse = models.ForeignKey("Warehouses", null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Warehouses(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


