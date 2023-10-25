from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ This class add the Product model to the admin panel """
    list_display = (
        "name",
        "product_type",
        "date_of_event",
        "category",
        "flavour",
        "price",
        "image",
    )

    ordering = ("price", )
