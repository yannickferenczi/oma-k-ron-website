from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from datetime import date

from .models import Product
from .forms import ProductForm


def all_products(request):
    """
    A view to display all products, including sorting and search queries.
    """
    products = Product.objects.filter(
        Q(product_type="1")
        | Q(date_of_event__gt=date.today())
    )
    query = None
    product_type = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "style":
                products = products.filter(product_type=1)
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "product_type" in request.GET:
            product_type = request.GET["product_type"]
            products = products.filter(product_type__name=product_type)
            # if product_type == 2:
            #     products = products.filter(date_of_event__gt=date.today)

        if "category" in request.GET:
            category = request.GET["category"]
            products = products.filter(category__name=category)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request,
                    "You did not enter any search criteria!",
                )
                return redirect(reverse('products'))
            queries = Q(
                name__icontains=query
            ) | Q(
                description__icontains=query
            ) | Q(
                flavour__icontains=query
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_product_type": product_type,
        "current_sorting": current_sorting,
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


@login_required
def add_product(request):
    """
    Add a product to the store

    This view is restricted to superusers only
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, this page is restricted to the store owners.",
        )
        return redirect(reverse("home"))
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Product successfully added!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to add product. Please ensure the form is valid",
            )
    else:
        form = ProductForm()
    template = "products/add_product.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store

    This view is restricted to superusers only
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, this page is restricted to the store owners.",
        )
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product successfully updated!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request,
                "Failed to update product. Please ensure the form is valid.",
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")
    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store

    This view is restricted to superusers only
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, this page is restricted to the store owners.",
        )
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product successfully deleted!")
        return redirect(reverse("products"))
    context = {
        "product": product,
    }
    return render(request, "products/delete_product.html", context)
