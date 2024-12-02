from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Product, Categories, Brand, DeliveryOptions, Hero, Blog
from django.db.models import Q
from .serializers import (
    ProductSerializer,
    CategoriesSerializer,
    UserSerializer,
    BrandsSerializer,
    DeliveryOptionsSerializer,
    HeroSerializer,
    BlogSerializer,
)
import random


@api_view(["GET"])
@permission_classes([AllowAny])
def endpoints(request):
    data = ["products/", "products/:id"]
    return Response(data)


class ProductsList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get("query", "")
        category_ids = request.GET.get("category_ids", "")
        brand_ids = request.GET.get("brand_ids", "")

        products = Product.objects.all()

        if query:
            products = products.filter(
                Q(name__icontains=query) | Q(details__icontains=query)
            )

        if category_ids:
            category_ids = category_ids.split(",")
            category_ids = [cat_id for cat_id in category_ids if cat_id.isdigit()]
            if category_ids:
                products = products.filter(category__id__in=category_ids)

        if brand_ids:
            brand_ids = brand_ids.split(",")
            brand_ids = [brand_id for brand_id in brand_ids if brand_id.isdigit()]
            if brand_ids:
                products = products.filter(brand__id__in=brand_ids)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class NewProducts(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        products = Product.objects.all().order_by("-added_at")[:10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    permission_classes = [AllowAny]

    def get_product(self, id):
        try:
            return Product.objects.get(pk=id)
        except:
            raise Response("Product Does not exist")

    def get(self, request, pk):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class PromotionalProductsView(APIView):
    def get(self, request):
        promotional_products = Product.objects.filter(quantity__gt=0).order_by(
            "-rating", "quantity"
        )[:4]

        if not promotional_products:
            all_products = list(Product.objects.all())
            promotional_products = random.sample(
                all_products, min(4, len(all_products))
            )

        serializer = ProductSerializer(promotional_products, many=True)

        return Response(serializer.data)


class CategoriesList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get("query", "")
        categories = Categories.objects.filter(Q(category__icontains=query))
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)


class BrandsList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get("query", "")
        brands = Brand.objects.filter(Q(brand__icontains=query))
        serializer = BrandsSerializer(brands, many=True)
        return Response(serializer.data)


class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class DeliveryOptionsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        deliveryOptions = DeliveryOptions.objects.all()
        serializer = DeliveryOptionsSerializer(deliveryOptions, many=True)
        return Response(serializer.data)
    
class HeroView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        hero_section_data = Hero.objects.all()
        serializer = HeroSerializer(hero_section_data, many=True)
        return Response(serializer.data)
    
class BlogView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)