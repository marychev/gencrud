from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm as DefaultUserChangeForm


class UserChangeForm(DefaultUserChangeForm):
    class Meta(DefaultUserChangeForm.Meta):
        model = User
