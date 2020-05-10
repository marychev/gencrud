from rest_framework import viewsets
from ..serialisers import ProductItemsSerializer
from catalog.models import ProductItem


class ProductItemsViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemsSerializer

