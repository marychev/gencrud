from catalog.views import CatalogView
from gen.tests.catalog import CatalogMockData, ProductMockData
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase


class CatalogDefaultViewTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.catalog = CatalogMockData().create()
        cls.product = ProductMockData(cls.catalog).create()
        cls.url = cls.catalog.get_absolute_url()
        cls.template_name = CatalogView.template_name

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.catalog.title)

    def test_page_contains_correct_seo(self):
        self.assert_contains_seo(self.catalog)
