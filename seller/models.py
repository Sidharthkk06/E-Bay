from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class SellerProduct(models.Model):
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # Image field for product images

    def __str__(self):
        return self.name
