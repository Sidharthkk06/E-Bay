from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Image field for product images

    def __str__(self):
        return self.product_name
