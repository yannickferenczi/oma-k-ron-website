from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product


def all_products(request):
    """
    A view to display all products, including sorting and search queries.
    """
    products = Product.objects.all()
    query = None
    product_type = None

    if request.GET:
        if "product_type" in request.GET:
            product_type = request.GET["product_type"]
            products = products.filter(product_type=product_type)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You did not enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(flavour__icontains=query)
            products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
    }
    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """
    A view to display details of a specific product.
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, 'products/product_detail.html', context)
