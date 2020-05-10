from django import forms
from django.contrib.auth.models import User
from users.models.user_profile import UserProfile
from order.models.order import Order


class OrderCreateForm(forms.ModelForm):
    """Форма оформления заказа."""
    def __init__(self, *args, **kwargs):

        # print(kwargs['initial']['cart'])
        # TODO: total_cost = kwargs['initial']['cart'].totalPrice
        total_cost = 888
        user = kwargs['initial']['user']
        super(OrderCreateForm, self).__init__(*args, **kwargs)

        try:
            address = user.userprofile.address
        except UserProfile.DoesNotExist:
            address = '-'

        self.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(id=user.id), empty_label=None, widget=forms.HiddenInput)
        self.fields['total_cost'] = forms.DecimalField(
            max_digits=10, decimal_places=2, initial=total_cost, widget=forms.HiddenInput)
        self.fields['first_name'] = forms.CharField(
            label='Имя', initial=user.first_name,
            widget=forms.TextInput(attrs={'placeholder': ':Александр', 'class': 'form-control'}))
        self.fields['last_name'] = forms.CharField(
            label='Фамилия', initial=user.last_name,
            widget=forms.TextInput(attrs={'placeholder': ':Иванов', 'class': 'form-control'}))
        self.fields['email'] = forms.EmailField(
            label='Email', initial=user.email,
            widget=forms.EmailInput(attrs={'placeholder': ':your-email@gmail.com', 'class': 'form-control'}))
        self.fields['address'] = forms.CharField(
            label='Адрес доставки', initial=address,
            widget=forms.TextInput(attrs={'placeholder': ':ул.Центральная д.152а оф.5', 'class': 'form-control'}))
        self.fields['ttn'] = forms.CharField(
            label='Товарно-транспортная накладная', required=False,
            widget=forms.TextInput(attrs={'placeholder': ':№  товарно-транспортной накладной', 'class': 'form-control'}))
        self.fields['comment'] = forms.CharField(
            label='Комментарий', required=False,
            widget=forms.Textarea(attrs={'placeholder': ':Комментарий к закакзу', 'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Order
        fields = ('user', 'first_name', 'last_name', 'email', 'address', 'ttn', 'comment', 'total_cost')
        # 'postal_code', 'city', )




