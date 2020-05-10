from rest_framework import status
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase
from gen.cart.cart import Cart
from gen.cart.strings import APP_NAME
from gen.cart.views import CartDetail
from gen.tests.cart import set_up_mock_data, MixinPostData


class CartPageViewTests(BaseDefaultViewTestCase, MixinPostData):
    PRODUCT_QTY = 5
    PRODUCT_ITEM_QTY = 2

    @classmethod
    def setUpTestData(cls):
        cls.url = '/{}/'.format(APP_NAME)
        cls.template_name = CartDetail.template_name
        set_up_mock_data(cls, CartPageViewTests.PRODUCT_QTY, CartPageViewTests.PRODUCT_ITEM_QTY)

    def test_correct_post_request_to_client(self):
        response = self.client.post(self.url, self._draft_post_data())
        session_cart = self.client.session.get(APP_NAME)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(Cart(self.client).get(), session_cart)
