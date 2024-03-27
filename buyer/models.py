from django.db import models
from django.contrib.auth.models import User
from seller.models import Product

# Create your models here.

class BuyerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()


class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(BuyerProfile, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid for {self.product.name} by {self.buyer.user.username} at {self.timestamp}"
