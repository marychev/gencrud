from django.urls import path
from django.contrib.auth.decorators import login_required
from gen.users.views import logout_view
from users.views import (Register, Login, Profile, Orders, OrderDetail, ReviewProducts)


urlpatterns = [
    path(r'login/', Login.as_view(), name='user_login'),
    path(r'logout/', logout_view, name='logout'),
    path(r'register/', Register.as_view(), name='user_register'),
    path(r'profile/', login_required(Profile.as_view()), name='profile'),
    path(r'orders/', login_required(Orders.as_view()), name='user_orders'),
    path(r'review/products/', login_required(ReviewProducts.as_view()), name='user_review_products'),
    path(r'<int:pk>/order/', login_required(OrderDetail.as_view()), name='user_order_detail'),
]
