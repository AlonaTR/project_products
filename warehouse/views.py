from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from warehouse.forms import ProductForm
from .models import Products, Warehouses
from django.core.paginator import Paginator


def pagination(request):
    contact_list = Products.objects.all()
    paginator = Paginator(contact_list, 10)

    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'warehouse/pagination.html', {'page_obj': page_obj,'products': Products.objects.all()})

def all_products(request):
    
    return render(request, 'warehouse/all_products.html', {'products': Products.objects.all()})

def warehouses(request):
    return render(request, 'warehouse/warehouses.html', {'warehouses': Warehouses.objects.all()})

def add_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_products')

    else:
        form = ProductForm()
    return render(request, 'warehouse/add_product.html', {'form': form})

def warehouse_products(request, warehouse):
    products = Products.objects.filter(warehouse_id=warehouse)
    warehouse_name = Warehouses.objects.get(id=warehouse).name
    return render(request, 'warehouse/one_warehouse.html', {'products': products, 'warehouse': warehouse_name})

def update_product(request, pk):
    product = Products.objects.get(id=pk)
    form= ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')

    else:
        form = ProductForm()
    return render(request, 'warehouse/update_product.html', {'form': form, 'product': product})
