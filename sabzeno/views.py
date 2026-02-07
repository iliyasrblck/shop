from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categoris = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categoris': categoris,
        'products': products,
    }
    return render(request, 'sabzeno/shop/list-products.html', context)


def product_detail(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug)

    return render(request, 'sabzeno/shop/detail-product.html', {'product': product})
