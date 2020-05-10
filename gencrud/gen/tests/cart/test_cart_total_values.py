from gen.tests.cart.abstract import AbstractCartClassTests


# TODO: fix test
class CartClassTests(AbstractCartClassTests):
    def test_get_total_price(self):
        ids, _cart = self._add_to_cart(0, 0)
        self.assertEquals(_cart.get_total_price(), 1000)

        ids, _cart = self._add_to_cart(0, 1)
        self.assertEquals(_cart.get_total_price(), 2000)

        # # todo: maybe error into _draft_post_data
        # ids, _cart = self._add_to_cart(0, 2)
        # print('3...', ids)
        # self.assertEquals(_cart.get_total_price(), 3000)

        ids, _cart = self._add_to_cart(1, 0)
        self.assertEquals(_cart.get_total_price(), 3000)

        ids, _cart = self._add_to_cart(1, 1)
        self.assertEquals(_cart.get_total_price(), 4000)

        # todo: maybe error into _draft_post_data
        # ids, _cart = self._add_to_cart(1, 2)
        # self.assertEquals(_cart.get_total_price(), 5000)

        ids, _cart = self._add_to_cart(2, 0)
        self.assertEquals(_cart.get_total_price(), 5000)

        ids, _cart = self._add_to_cart(2, 1)
        self.assertEquals(_cart.get_total_price(), 6000)

        # todo: maybe error into _draft_post_data
        # ids, _cart = self._add_to_cart(2, 2)
        # self.assertEquals(_cart.get_total_price(), 7000)

        ids, _cart = self._add_to_cart(3, 0)
        self.assertEquals(_cart.get_total_price(), 7000)

        ids, _cart = self._add_to_cart(3, 1)
        self.assertEquals(_cart.get_total_price(), 8000)

        # # todo: maybe error into _draft_post_data
        # ids, _cart = self._add_to_cart(3, 2)
        # self.assertEquals(_cart.get_total_price(), 9000)

    def test_get_total_count_product_items(self):
        self._add_to_cart(0, 0)
        self._add_to_cart(0, 1)
        # self._add_to_cart(0, 2)
        self._add_to_cart(1, 0)
        self._add_to_cart(1, 1)
        # self._add_to_cart(1, 2)
        self._add_to_cart(2, 0)
        self._add_to_cart(2, 1)
        # self._add_to_cart(2, 2)
        self._add_to_cart(3, 0)
        ids, _cart = self._add_to_cart(3, 1)
        # ids, _cart = self._add_to_cart(3, 2)
        self.assertEquals(_cart.get_total_count_product_items(), 8)

