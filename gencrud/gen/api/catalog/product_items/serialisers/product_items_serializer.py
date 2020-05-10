from rest_framework import serializers
from catalog.models import ProductItem


class ProductItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['pk', 'name', 'price', 'price_discount', 'product']
