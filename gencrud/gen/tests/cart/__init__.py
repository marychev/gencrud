from gen.tests.catalog import CatalogMockData, ProductMockData, ProductItemsMockData


def set_up_mock_data(cls, product_qty=5, product_item_qty=3):
    cls.catalog = CatalogMockData().create()
    cls.products = ProductMockData(cls.catalog, product_qty).create_list()
    cls.product_items = [
        ProductItemsMockData(cls.products[i], product_item_qty).create_list()
        for i in range(product_qty)
    ]


class MixinPostData:
    def _draft_post_data(self, index_product=0, index_product_item=0):
        count = 1
        products = self.products[index_product],
        product_item = self.product_items[index_product][index_product_item]
        product = {
            'id': products[0].id,
            'title': products[0].title,
        }

        product_items = {
            'productItems[{}][id]'.format(index_product_item): product_item.id,
            'productItems[{}][title]'.format(index_product_item): product_item.name,
            'productItems[{}][count]'.format(index_product_item): [count],
            'productItems[{}][price]'.format(index_product_item): ProductItemsMockData.PRICE,
        }

        product_items.update(product)
        return product_items
