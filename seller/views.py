from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from seller.models import Product, Property, QuantityOfProduct
from seller.serializers import ProductSerializer, PropertySerializer, QuantityOfProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class QuantityOfProductViewSet(ModelViewSet):
    queryset = QuantityOfProduct.objects.all()
    serializer_class = QuantityOfProductSerializer
