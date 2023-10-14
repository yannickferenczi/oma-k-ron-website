from django.contrib import admin

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total", )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, )

    readonly_fields = (
        "order_number",
        "date_of_order",
        "delivery_costs",
        "order_value",
        "total",
        "original_cart",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "date_of_order",
        "full_name",
        "user_profile",
        "email",
        "phone_number",
        "street_address_1",
        "street_address_2",
        "postcode",
        "city",
        "county",
        "country",
        "order_value",
        "delivery_costs",
        "total",
        "original_cart",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "full_name",
        "date_of_order",
        "delivery_costs",
        "order_value",
        "total",
    )

    ordering = ("-date_of_order", )