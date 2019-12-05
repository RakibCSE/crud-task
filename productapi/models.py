from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=10)
    slug = models.SlugField(max_length=250)
    available = models.BooleanField()

    def __str__(self):
        return self.name


class Attribute(models.Model):
    product = models.ForeignKey(Product, related_name="attributes", on_delete=models.PROTECT)
    color = models.CharField(max_length=15)
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.color + " " + self.size


class Price(models.Model):
    product = models.ForeignKey(Product, related_name="prices", on_delete=models.PROTECT)
    price = models.IntegerField()
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return str(self.price)
