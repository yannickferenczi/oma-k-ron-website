from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, )
    product_type = models.CharField(max_length=250, )
    style = models.CharField(max_length=250, )
    flavour = models.CharField(max_length=250, )
    description = models.CharField(max_length=250, )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
