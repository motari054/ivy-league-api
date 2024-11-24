from django.contrib import admin
from .models import AccessToken, Payments

admin.site.register(AccessToken)
admin.site.register(Payments)