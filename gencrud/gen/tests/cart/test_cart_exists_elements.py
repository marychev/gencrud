from gen.cart.cart import Cart
from gen.tests.cart.abstract import AbstractCartClassTests


class CartClassTests(AbstractCartClassTests):
    PRODUCT_QTY = AbstractCartClassTests.PRODUCT_QTY
    PRODUCT_ITEM_QTY = AbstractCartClassTests.PRODUCT_ITEM_QTY

    def test_exist_product(self):
        ids, _cart = self._add_to_cart(0, 0)
        self.assertIs(_cart.exist_product(ids[0]), True)

    def test_exist_product_item(self):
        self.client.post(self.url, {})
        added_product_item_ids = []

        product_index = 1
        product_item_index = 0
        post_data = self._draft_post_data(product_index, product_item_index)
        post_product_item_id = post_data.get('productItems[{}][id]'.format(product_item_index))
        cart = Cart(self.client)
        self.assertIs(cart.exist_product_item(post_product_item_id), False)
        self.client.post(self.url, post_data)
        cart = Cart(self.client)
        self.assertIs(cart.exist_product_item(post_product_item_id), True)
        added_product_item_ids.append(post_product_item_id)

        product_index = 0
        product_item_index = 2
        post_data = self._draft_post_data(product_index, product_item_index)
        post_product_item_id = post_data.get('productItems[{}][id]'.format(product_item_index))
        cart = Cart(self.client)
        self.assertIs(cart.exist_product_item(post_product_item_id), False)
        self.client.post(self.url, post_data)
        cart = Cart(self.client)
        self.assertIs(cart.exist_product_item(post_product_item_id), True)
        added_product_item_ids.append(post_product_item_id)

        ids, _cart = self._add_to_cart(0, 0)
        self.assertIs(_cart.exist_product_item(ids[1]), True)
        added_product_item_ids.append(ids[1])

        ids, _cart = self._add_to_cart(0, 1)
        self.assertIs(_cart.exist_product_item(ids[1]), True)
        added_product_item_ids.append(ids[1])

        ids, _cart = self._add_to_cart(3, 2)
        self.assertIs(_cart.exist_product_item(ids[1]), True)
        added_product_item_ids.append(ids[1])

        ids, _cart = self._add_to_cart(CartClassTests.PRODUCT_QTY-1, CartClassTests.PRODUCT_ITEM_QTY-1)
        self.assertIs(_cart.exist_product_item(ids[1]), True)
        added_product_item_ids.append(ids[1])

        cart = Cart(self.client)
        for i in added_product_item_ids:
            self.assertIs(_cart.exist_product_item(i), True)
            self.assertIs(cart.exist_product_item(i), True)

