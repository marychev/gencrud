from catalog.views import CatalogView
from gen.tests.catalog import CatalogMockData, ProductMockData
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase


class CatalogPaginationGetRequestTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.product_count = 42
        cls.catalog = CatalogMockData().create()
        cls.products = ProductMockData(cls.catalog, cls.product_count).create_list()
        cls.url = cls.catalog.get_absolute_url()
        cls.template_name = CatalogView.template_name

    def test_two_page_status_code(self):
        url_get_params = '{}?page=2'.format(self.url)
        self.check_status_code_equals(url_get_params)

    def test_not_exists_page_return_last_page(self):
        url_get_params = '{}?page={}'.format(self.url, self.product_count)
        self.check_status_code_equals(url_get_params)

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.catalog.title)

    def test_page_contains_correct_seo(self):
        self.assert_contains_seo(self.catalog)
