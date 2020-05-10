from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartDetail.as_view(), name='cart_detail'),
    path('add/', views.CartDetail.as_view(), name='add_to_cart'),
    path('remove/<int:product_item_id>/', views.cart_remove, name='cart-remove'),
    path('clear/', views.cart_clear, name='cart_clear'),
]


