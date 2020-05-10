from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        label='Кол-во', min_value=0, initial=0, required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'quantity',
            'min': '1',
            'required': True,
        })
    )
    is_update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput,
        help_text='был ли товар добавлен в корзину')

