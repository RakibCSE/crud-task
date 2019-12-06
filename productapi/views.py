from rest_framework import generics

from .models import Product, Attribute, Price
from .serializers import ProductSerializer, AttributeSerializer, PriceSerializer


class ProductList(generics.ListCreateAPIView):
    """
    Product list API View.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Product detail API View.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AttributeList(generics.ListCreateAPIView):
    """
    Attribute list API View.
    """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Attribute detail API View.
    """
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class PriceList(generics.ListCreateAPIView):
    """
    Price list API View.
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Price detail API View.
    """
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
