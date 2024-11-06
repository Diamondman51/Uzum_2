from rest_framework import serializers

from seller.models import Product, Property, QuantityOfProduct


class ProductSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']


class QuantitySerializer(serializers.ModelSerializer):
    product = ProductSerializer2()

    class Meta:
        model = QuantityOfProduct
        fields = ['product']


class PropertySerializer(serializers.ModelSerializer):
    quantity_id = QuantitySerializer()

    class Meta:
        model = Property
        fields = "__all__"


class QuantityOfProductSerializer(serializers.ModelSerializer):
    property_set = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = QuantityOfProduct
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    quantityofproduct_set = QuantityOfProductSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "seller_id", "name", "description", "quantityofproduct_set",]
