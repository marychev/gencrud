from gen.order.forms.product_claim import ProductClaimForm
from gen.tests.order.forms.mixins import AnonymousUserMixinTest
from gen.tests.catalog import CatalogMockData, ProductMockData


class ProductClaimFormModelAnonymousUserTest(AnonymousUserMixinTest):
    def setUp(self):
        super().setUp()
        catalog = CatalogMockData().create()
        self.product = ProductMockData(catalog).create()

    @property
    def valid_data(self):
        return {
            'user': self.user.pk,
            'email': 'anonymous@email.com',
            'product': self.product.pk,
            'product_items': None,
            'comment': 'Hello'
        }

    def test_valid(self):
        form = ProductClaimForm(self.valid_data).form
        self.assertTrue(form.is_valid())

    def test_no_valid(self):
        post = self.valid_data.copy()
        post.update({'email': 'no-email.com'})
        form = ProductClaimForm(post).form
        self.assertFalse(form.is_valid())

        post = self.valid_data.copy()
        post.update({'product': ''})
        form = ProductClaimForm(post).form
        self.assertFalse(form.is_valid())

        form = ProductClaimForm({}).form
        self.assertFalse(form.is_valid())
