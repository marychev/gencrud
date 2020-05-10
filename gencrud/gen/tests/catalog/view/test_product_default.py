from catalog.views import ProductDetail
from gen.tests.catalog import CatalogMockData, ProductMockData
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase


class ProductDetailWithoutProductItemsViewTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.catalog = CatalogMockData().create()
        cls.product = ProductMockData(cls.catalog).create()
        cls.url = cls.product.get_absolute_url()
        cls.template_name = ProductDetail.template_name

    def test_contains_correct_h1_has_detail_link_without_items_product(self):
        response = self.client.get(self.url)
        self.assertNotContains(response, 'name="product_item"')
        self.assertContains(response, 'href="#detail">{}</a>'.format(self.product.title))

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.product.title)

    def test_contains_correct_seo_title(self):
        self.assert_contains_seo(self.product)


