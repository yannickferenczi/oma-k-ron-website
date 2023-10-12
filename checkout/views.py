from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from cart.contexts import cart_contents


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    template = "checkout/checkout.html"
    if request.method == "POST":
        cart = request.session.get("cart", {})
        form_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "street_address_1": request.POST["street_address_1"],
            "street_address_2": request.POST["street_address_2"],
            "postcode": request.POST["postcode"],
            "city": request.POST["city"],
            "county": request.POST["county"],
            "country": request.POST["country"],
        }
        order_form = OrderForm(form_data)
        context = {
            "order_form": order_form,
        }
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in cart.items():
                product = Product.objects.get(id=item_id)
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                )
                order_line_item.save()
            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(request, "There was an error with your form. \
                Please double check your information and resubmit the form.")
    else:
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(request, "Your cart is currently empty.")
            return redirect(reverse("products"))

        current_cart = cart_contents(request)
        total = current_cart["total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if not stripe_public_key:
            messages.warning(request, "Stripe public key is missing. \
                Did you forget to set it in your environment?")

        order_form = OrderForm()
        context = {
            "order_form": order_form,
            "stripe_public_key": stripe_public_key,
            "client_secret": intent.client_secret,
        }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.")

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }
    return render(request, template, context)
