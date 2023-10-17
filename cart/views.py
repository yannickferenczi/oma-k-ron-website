from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def display_cart(request):
    """
    A view to display the cart content
    """
    context = {
        "on_cart_page": True,
    }
    return render(request, "cart/cart.html", context)


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
            f"The quantity of <strong>{product.name}</strong> has been \
                successfully updated in your cart."
        )
    else:
        cart[item_id] = quantity
        messages.success(
            request,
            f"<strong>{product.name}</strong> has been successfully \
                added to your cart."
        )
    request.session["cart"] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request,
            f"The quantity of {product.name} has been successfully \
                updated to {cart[item_id]}.",
        )
    else:
        cart.pop(item_id)
        messages.success(
            request,
            f"{product.name} has been successfully \
                removed from your shopping cart.",
            )
    request.session["cart"] = cart
    return redirect(reverse("cart"))
