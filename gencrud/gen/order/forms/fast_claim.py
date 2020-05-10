from django import forms

from gen.order.forms.abstract_claim import AbstractClaimForm
from order.models import FastClaim


class FastClaimAnonymousModelForm(forms.ModelForm):
    class Meta:
        model = FastClaim
        fields = ('email', 'phone', 'typeof', 'comment')
        widgets = {
            'typeof': forms.Select(attrs={'class': 'form-control'})
        }


class FastClaimUserModelForm(forms.ModelForm):
    class Meta:
        model = FastClaim
        fields = ('user', 'email', 'phone', 'typeof', 'comment')


class FastClaimForm(AbstractClaimForm):
    def __init__(self, post):
        self.user_form = FastClaimUserModelForm
        self.anonymous_form = FastClaimAnonymousModelForm
        super().__init__(post)
