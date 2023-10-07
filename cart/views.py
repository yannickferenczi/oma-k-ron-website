from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product


def display_cart(request):
    """
    A view to display the cart content
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """
    Add a quantity of the selected product to the cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            f"The quantity of <strong>{product.name}</strong> has been successfully \
                updated in your cart."
        )
    else:
        cart[item_id] = quantity
        messages.success(
            request,
            f"<strong>{product.name}</strong> has been successfully added to your cart."
        )
    request.session["cart"] = cart
    return redirect(redirect_url)
