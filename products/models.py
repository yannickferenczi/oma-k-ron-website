from django.db import models


class ProductType(models.Model):
    """
    A model to define if the product is a macaron or an event
    """
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        ordering = ["product_type", "date_of_event"]
    name = models.CharField(max_length=250, )
    product_type = models.ForeignKey(
        'ProductType',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    style = models.CharField(max_length=250, blank=True, null=True)
    flavour = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.IntegerField(blank=True, null=True)
    date_of_event = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
