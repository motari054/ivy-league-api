from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Product,
    Categories,
    User,
    Brand,
    DeliveryOptions,
    Hero,
    Blogs,
    TikTok,
)


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class BrandsSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    effective_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            "id", "name", "brand", "category", "price", "quantity", "details",
            "how_to_use", "rating", "image", "added_at", "sold", "on_offer",
            "discount", "discount_end_date", "effective_price"
        ]
    
    def get_effective_price(self, obj):
        return obj.effective_price()



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "second_name", "email"]


class DeliveryOptionsSerializer(ModelSerializer):
    class Meta:
        model = DeliveryOptions
        fields = "__all__"


class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class BlogsSerializer(ModelSerializer):
    class Meta:
        model = Blogs
        fields = "__all__"

class TikTokSerializer(ModelSerializer):
    class Meta:
        model = TikTok
        fields = "__all__"