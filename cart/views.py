from django.shortcuts import render


def display_cart(request):
    """
    A view to display the cart content
    """
    return render(request, "cart/cart.html")
