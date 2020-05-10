from catalog.models import Catalog, Product, ProductItem
from gen.catalog.strings import APP_NAME
from gen.tests.mock_data import MockModelData


class CatalogMockData(MockModelData):
    def __init__(self):
        super().__init__()
        self._model = Catalog

    @property
    def title(self):
        return 'Title %s #1' % APP_NAME

    @property
    def default_object(self):
        return {
            'title': self.title,
            'is_show': True
        }


class ProductMockData(MockModelData):
    def __init__(self, catalog, count=50):
        super().__init__()

        self._model = Product
        self._title = 'Title {} {}'
        self.catalog = catalog
        self.count = count

    @property
    def default_object(self):
        return {
            'title': self.title,
            'is_show': True,
        }

    def create(self):
        product = self.model.objects.create(**self.default_object)
        product.catalogs.add(self.catalog)
        return product


class ProductItemsMockData(MockModelData):
    PRICE = 1000

    def __init__(self, product, count=4):
        super().__init__()

        self._model = ProductItem
        self._title = 'Title {} {}'
        self.product = product
        self.count = count

    @property
    def default_object(self):
        return {
            'name': self.title,
            'price': ProductItemsMockData.PRICE,
            'product': self.product
        }
