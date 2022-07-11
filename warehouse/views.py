from django.shortcuts import render
from .models import Products

def all_products(request):
    return render(request, 'warehouse/all_products.html', {'products': Products.objects.all()})

def warehouses(request):
    return render(request, 'warehouse/warehouses.html', {'warehouses': Products.objects.all()})
