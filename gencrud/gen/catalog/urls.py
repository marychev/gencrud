from django.urls import path
from catalog.views import CatalogView, ProductDetail, ProductCommentView
from gen.catalog.strings import URL_PREFIX_CATALOG

urlpatterns = [
    path('<str:slug>/', CatalogView.as_view(), name=URL_PREFIX_CATALOG),
    path(
        '<str:{}>/<str:product>/'.format(URL_PREFIX_CATALOG),
        ProductDetail.as_view(), name='product_detail'
    ),
    path('comment/product/<int:product_id>/', ProductCommentView.as_view(), name='product_comment'),
]

