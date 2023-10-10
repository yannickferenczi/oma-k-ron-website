from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        messages.error(request, "Your cart is currently empty.")
        return redirect(reverse("products"))
    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51NpdCJJJO4onEsLlTcVo4PBWAmZ1lH7qcBWMyx1hNYYnXQbe6mrSUx6aepdjtYRXIJODpDcKLDgpsNGYA44y4iv2002dQPIWJc",
        "client_secret": "test client secret"
    }
    return render(request, template, context)
