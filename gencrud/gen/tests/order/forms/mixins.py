from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User


def create_simple_user():
    return User.objects.create_user(
        username='simple_user',
        email='simple_user@mail.com',
        password='gen_crud_888'
    )


class AuthUserMixinTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = create_simple_user()


class AnonymousUserMixinTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AnonymousUser()
