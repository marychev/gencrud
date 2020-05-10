from django import forms
from gen.order.forms.abstract_claim import AbstractClaimForm
from order.models import ProductClaim


class ProductClaimAnonymousModelForm(forms.ModelForm):
    class Meta:
        model = ProductClaim
        fields = ('email', 'phone', 'product', 'product_items', 'comment')


class ProductClaimUserModelForm(forms.ModelForm):
    class Meta:
        model = ProductClaim
        fields = ('email', 'phone', 'user', 'product', 'product_items', 'comment')


class ProductClaimForm(AbstractClaimForm):
    def __init__(self, post):
        self.user_form = ProductClaimUserModelForm
        self.anonymous_form = ProductClaimAnonymousModelForm
        super().__init__(post)
