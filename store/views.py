from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    categories = Category.objects.prefetch_related('products').all()
    products = Product.objects.filter(available=True)[:20]
    return render(request, 'store/index.html', {'categories': categories, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})
