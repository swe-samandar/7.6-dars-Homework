from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name