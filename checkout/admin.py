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
    )

    fields = (
        "order_number",
        "full_name",
        "email",
        "phone_number",
        "street_address_1",
        "street_address_2",
        "postcode",
        "city",
        "county",
        "country",
        "date_of_order",
        "delivery_costs",
        "order_value",
        "total",
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