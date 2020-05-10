from rest_framework import serializers
from catalog.models import Product, ProductItem
from gen.api.catalog.product_items.serialisers import ProductItemsSerializer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'title', 'catalogs', 'price', 'product_items']

    price = serializers.SerializerMethodField()
    product_items = serializers.SerializerMethodField()

    def get_price(self, obj):
        return obj.get_price()

    def get_product_items(self, obj):
        qs = ProductItem.objects.filter(product=obj, product__is_show=True)
        return ProductItemsSerializer(qs, many=True).data
