from rest_framework import serializers

from .models import Product, Attribute, Price


class ProductSerializer(serializers.ModelSerializer):
    """
    Product serializer
    """

    class Meta:
        model = Product
        fields = '__all__'


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Attribute serializer to show the product attributes list.
    """

    def __init__(self, *args, **kwargs):
        """
        For multiple attributes used many=True
        Args:
            *args:
            **kwargs:
        """
        many = kwargs.pop('many', True)
        super(AttributeSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Attribute
        fields = ('color', 'size', 'product',)


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Price serializer to show the prices over the API call.
    """

    def __init__(self, *args, **kwargs):
        """
        For multiple attributes used many=True
        Args:
            *args:
            **kwargs:
        """
        many = kwargs.pop('many', True)
        super(PriceSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Price
        fields = ('product', 'price', 'start_date', 'end_date',)
