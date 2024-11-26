from rest_framework.serializers import ModelSerializer
from .models import Product, Categories, User, Brand, DeliveryOptions, Hero

class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class BrandsSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    category = CategoriesSerializer()
    brand = BrandsSerializer()
    class Meta:
        model = Product
        fields = ['id','name', 'details', 'how_to_use', 'price', 'rating', 'image', 'category', 'brand']
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'email']

class DeliveryOptionsSerializer(ModelSerializer):
    class Meta:
        model = DeliveryOptions
        fields = '__all__'

class HeroSerializer(ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'