from django.urls import path
from order.views import OrderCreate, OrderCreated, ProductClaimFormView, FastClaimFormView
# , AjaxGetProduct, ClaimCallerView,


urlpatterns = [
    path(r'create/', OrderCreate.as_view(), name='order-create'),
    path(r'<int:pk>/created/', OrderCreated.as_view(), name='order-created'),

    path(r'fast-claim-form/create/', FastClaimFormView.as_view(), name='fast-claim-form'),
    path(r'product-claim-form/create/', ProductClaimFormView.as_view(), name='product-claim-form'),
    # path(r'claim-caller/create/', ClaimCallerView.as_view(), name='claim_caller'),
]
