from rest_framework import viewsets
from ..serialisers import ProductSerializer
from catalog.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

