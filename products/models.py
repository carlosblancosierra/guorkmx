from django.db import models


class ProductManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ProductManager, self).filter(draft=False)


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    objects = ProductManager()
