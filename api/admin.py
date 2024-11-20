from django.contrib import admin
from .models import User, Product, Categories, Brand, DeliveryOptions

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(DeliveryOptions)