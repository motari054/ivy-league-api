from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    second_name = models.CharField(max_length=100, null=True)
    username = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Categories(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Brand(models.Model):
    brand = models.CharField(max_length=100)
    def __str__(self):
        return self.brand

class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    how_to_use = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    image = CloudinaryField('image')
    quantity = models.IntegerField(default=0)
    added_at = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name='products')

    def __str__(self):
        return self.name

class DeliveryOptions(models.Model):
    label = models.CharField(max_length=200)
    price= models.IntegerField()

    def __str__(self):
        return f"{self.label} - Ksh.{self.price}"
    
    class Meta:
        verbose_name = "Delivery Option"
        verbose_name_plural = "Delivery Options"

class Deliveries(models.Model):
    customer_name = models.CharField(max_length=200)
    primary_number = models.IntegerField()
    secondary_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=250)
    town = models.CharField(max_length=200)
    amount_paid = models.IntegerField()
    mpesa_transaction_code = models.CharField(max_length=200)
    delivery_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.town}"
    
    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = "Deliveries"
