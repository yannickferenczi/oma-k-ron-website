import json
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def cart_contents(request):
    cart_items = []
    order_value = 0
    product_count = 0
    delivery_costs = 0
    cart = request.session.get("cart", {})
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price
        order_value += subtotal
        product_count += quantity
        cart_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "subtotal": subtotal,
                "product": product,
            }
        )
    for item in cart_items:
        if item["product"].product_type.lower() == "tower":
            delivery_costs = settings.DELIVERY_COSTS_CELEBRATIONS
            break
        else:
            delivery_costs = settings.DELIVERY_COSTS_BASICS
    total = order_value + delivery_costs
    context = {
        "cart_items": cart_items,
        "order_value": order_value,
        "product_count": product_count,
        "delivery_costs": delivery_costs,
        "total": total,
    }

    return context
