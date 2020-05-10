import datetime
from django import forms
from users.models.user_profile import UserProfile


class ProfileForm(forms.Form):
    """
    Form for user to update their own profile details
    (excluding links which are handled by a separate formset)
    """
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        try:
            patronymic = self.user.userprofile.patronymic
            phone = self.user.userprofile.phone
            birthday = self.user.userprofile.birthday
            address = self.user.userprofile.address
        except UserProfile.DoesNotExist:
            patronymic = None
            phone = None
            birthday = None
            address = None

        self.fields['first_name'] = forms.CharField(
            max_length=30, label='Имя*', initial=self.user.first_name,
            widget=forms.TextInput(attrs={'placeholder': ':Имя', 'class': 'form-control'}))
        self.fields['last_name'] = forms.CharField(
            max_length=30, label='Фамилия*', initial=self.user.last_name,
            widget=forms.TextInput(attrs={'placeholder': ':Фамилия', 'class': 'form-control'}))
        self.fields['patronymic'] = forms.CharField(
            max_length=30, label='Отчество', initial=patronymic, required=False,
            widget=forms.TextInput(attrs={'placeholder': ':Отчество', 'class': 'form-control'}))
        self.fields['phone'] = forms.CharField(
            max_length=30, label='Телефон*', initial=phone,
            widget=forms.TextInput(attrs={'placeholder': ':Телефон', 'class': 'form-control jsPhoneInput'}))
        self.fields['birthday'] = forms.DateField(
            label='День рождения', initial=birthday, required=False,
            widget=forms.DateInput(attrs={'placeholder': ':День рождения', 'class': 'form-control jsDatepicker'}))
        self.fields['address'] = forms.CharField(
            max_length=512, label='Адрес', initial=address, required=False,
            widget=forms.TextInput(attrs={'placeholder': ':Адрес', 'class': 'form-control'}))

    def save(self):
        birthday = None
        if self.cleaned_data['birthday']:
            str_birthday = str(self.cleaned_data['birthday']).replace('.', '-')
            birthday = datetime.datetime.strptime(str_birthday, "%Y-%m-%d").date()

        UserProfile.objects.update_or_create(
            user=self.user,
            defaults={
                'patronymic': self.cleaned_data['patronymic'],
                'phone': self.cleaned_data['phone'],
                'birthday': birthday,
                'address': self.cleaned_data['address']
                })


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  HELPFUL
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class UserProfileForm(forms.ModelForm):
#     """
#     Форма для пользователя, чтобы обновить свои собственные данные профиля
#     (исключая ссылки, которые обрабатываются отдельной формой)
#     """
#     # def __init__(self, *args, **kwargs):
#     #     # magic
#     #     self.user = kwargs['instance'].user
#     #     user_kwargs = kwargs.copy()
#     #     user_kwargs['instance'] = self.user
#     #     self.user_form = UserProfileForm(*args, **user_kwargs)
#     #     # magic end
#     #
#     #     super(UserProfileForm, self).__init__(*args, **kwargs)
#     #
#     #     self.fields.update(self.user_form.fields)
#     #     self.initial.update(self.user_form.initial)
#     #     # self.user = kwargs.pop('user', None)
#
#     first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     patronymic = forms.CharField(required=False, label='Отчество', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     birthday = forms.DateField(label='День рождения', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
#     phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7(888)-88-88'}))
#     address = forms.CharField(
#         label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}),
#         help_text='Адрес по умолчанию, для доставки товара.')
#
#     class Meta:
#         model = UserProfile
#         fields = ('first_name', 'last_name', 'patronymic', 'birthday', 'phone', 'address')
#
#     def save(self, user=None, request=None):
#         user_profile = super(UserProfileForm, self).save(commit=False)
#         if user:
#             user_profile.user = user
#             # user_profile.phone = request.POST.get('phone', '')
#         user_profile.save()
#         return user_profile
