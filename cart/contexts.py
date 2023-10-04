from django.conf import settings


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    delivery_costs = settings.DELIVERY_COSTS
    total_with_delivery = total + delivery_costs
    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "delivery_costs": delivery_costs,
        "total_with_delivery": total_with_delivery,
    }

    return context