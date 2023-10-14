import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    This class creates a table to save Order instances in the database.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address_1 = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    street_address_2 = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )
    postcode = models.CharField(max_length=5, null=False, blank=False)
    city = models.CharField(max_length=250, null=False, blank=False)
    county = models.CharField(max_length=250, null=True, blank=True)
    country = CountryField(
        blank_label="Germany"
    )
    date_of_order = models.DateTimeField(auto_now_add=True)
    delivery_costs = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        default=0,
    )
    order_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0,
    )
    total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0,
    )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        default='',
    )


    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the total of the order each time a line item is added.
        """
        self.order_value = self.lineitems.aggregate(
            Sum("lineitem_total"))["lineitem_total__sum"] or 0
        if self.order_value == 0:
            self.delivery_costs = 0
        else:
            for item in self.lineitems.all():
                if item.product.product_type.lower() == "tower":
                    self.delivery_costs = settings.DELIVERY_COSTS_CELEBRATIONS
                    break
                else:
                    self.delivery_costs = settings.DELIVERY_COSTS_BASICS
        self.total = self.order_value + self.delivery_costs
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number if it
        has not been set yet.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    This class creates a table to save OrderLineItem instances in the database.

    A new instance will be created for every new product added to the cart.
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems',
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} on order {self.order.order_number}"
