# from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import views as auth_views


class PasswordResetView(auth_views.PasswordResetView):
    subject_template_name = 'registration/password_reset_subject.txt'
