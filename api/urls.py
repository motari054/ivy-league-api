from django.urls import path
from . import views

urlpatterns = [
    path("", views.endpoints),
    path("products/", views.ProductsList.as_view()),
    path("products/<str:pk>/", views.ProductDetail.as_view()),
    path("categories/", views.CategoriesList.as_view()),
    path("brands/", views.BrandsList.as_view()),
    path("user/details", views.UserDetailsView.as_view()),
    path("new/", views.NewProducts.as_view()),
    path("delivery-options/", views.DeliveryOptionsView.as_view()),
    path("promotional/", views.PromotionalProductsView.as_view()),
    path("hero/", views.HeroView.as_view()),
    path("blogs/", views.BlogView.as_view()),
]
