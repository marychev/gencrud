from django.urls import path, include
from rest_framework import routers
from gen.api.users.views import UserViewSet, UserProfileViewSet
from gen.api.catalog.product.views import ProductViewSet
from gen.api.catalog.product_items.views import ProductItemsViewSet
from gen.api.param.views.api_param_list import ParamAllListAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', UserProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-items', ProductItemsViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("params/", ParamAllListAPIView.as_view(), name="params_all_list"),
]

