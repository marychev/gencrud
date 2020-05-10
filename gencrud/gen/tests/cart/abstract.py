from django.test import TestCase
from gen.cart.cart import Cart
from gen.cart.strings import APP_NAME
from gen.tests.cart import set_up_mock_data, MixinPostData


class AbstractCartClassTests(TestCase, MixinPostData):
    PRODUCT_QTY = 5
    PRODUCT_ITEM_QTY = 3

    @classmethod
    def setUpTestData(cls):
        cls.url = '/{}/'.format(APP_NAME)
        set_up_mock_data(cls, AbstractCartClassTests.PRODUCT_QTY, AbstractCartClassTests.PRODUCT_ITEM_QTY)

    def _add_to_cart(self, product_index, product_item_index):
        post_data = self._draft_post_data(product_index, product_item_index)
        self.client.post(self.url, post_data)

        post_product_id = post_data.get('id')
        post_product_item_id = post_data.get('productItems[{}][id]'.format(product_item_index))
        return [
                   post_product_id,
                   post_product_item_id
               ], Cart(self.client)
