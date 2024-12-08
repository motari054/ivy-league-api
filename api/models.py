from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    second_name = models.CharField(max_length=100, null=True)
    username = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="products"
    )
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    details = models.TextField()
    how_to_use = models.TextField()
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=4,
        validators=[
            MinValueValidator(1.1),
            MaxValueValidator(5.0),
        ],
    )
    image = CloudinaryField("image")
    added_at = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)
    on_offer = models.BooleanField(default=False)
    discount = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(90.0),
        ],
    )
    discount_end_date = models.DateTimeField(null=True, blank=True)

    def effective_price(self):
        """Calculate the effective price after discount."""
        if self.discount:
            return self.price * (1 - (self.discount / 100))
        return self.price

    def __str__(self):
        return self.name


class DeliveryOptions(models.Model):
    label = models.CharField(max_length=200)
    price = models.IntegerField()

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
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

class Hero(models.Model):
    image = CloudinaryField("image")
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    class Meta:
        verbose_name = "Hero"
        verbose_name_plural = "Hero"

    def __str__(self):
        return self.title

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=300)
    thumbnail = CloudinaryField('image')
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"



class TikTok(models.Model):
    video = CloudinaryField("video", resource_type="video")
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "TikTok"
        verbose_name_plural = "TikTok"
