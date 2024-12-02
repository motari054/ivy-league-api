from django.contrib import admin
from .models import User, Product, Categories, Brand, DeliveryOptions, Deliveries, Hero

admin.site.register(User)
admin.site.register(DeliveryOptions)
admin.site.register(Product)
admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Deliveries)
admin.site.register(Hero)
