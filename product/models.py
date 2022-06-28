from django.db import models
from django.contrib.auth import get_user_model

from applications.category.models import Category

User = get_user_model()


class Product(models.Model):
    title = models.CharField(max_length=80, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Category')
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=1)
    logo = models.ImageField(blank=True, null=True, upload_to='images', default="images/macbookpro13.jpeg")

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Image')

    def __str__(self):
        return self.product.title


