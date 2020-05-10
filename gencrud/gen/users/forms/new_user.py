from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': forms.EmailField}

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Email'

    def clean_email(self):
        try:
            email = validate_email(self.cleaned_data.get("email"))
            self.instance.email = self.cleaned_data.get('email')
        except forms.ValidationError:
            raise ('|x_x|: ERROR {0} {1}'.format(self.__class__.__name__, self.errors), )
        return email

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=commit)
        user.email = user.username

        if commit:
            user.save()
        return user
