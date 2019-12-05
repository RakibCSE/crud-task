from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.ProductList.as_view(), name="product-list"),
    path("products/<int:pk>/", views.ProductDetail.as_view(), name="product-detail"),
    path("products/<int:pk>/attributes/", views.AttributeList.as_view(), name="attribute-list"),
    path("attributes/<int:pk>/", views.AttributeDetail.as_view(), name="attribute-detail"),
    path("products/<int:pk>/prices/", views.PriceList.as_view(), name="price-list"),
    path("prices/<int:pk>/", views.PriceDetail.as_view(), name="price-detail"),
]
