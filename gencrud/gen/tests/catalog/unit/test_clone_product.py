from django.test import TestCase, Client
from gen.tests.catalog import CatalogMockData, ProductMockData
from gen.abstract.mixins.clone import CloneObjectMixin


class CloneProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.catalog = CatalogMockData().create()
        cls.product = ProductMockData(cls.catalog).create()

    def setUp(self):
        self.clone = CloneObjectMixin()

    def test_clone_with_one_catalog(self):
        expected_title = self.clone.clone_format(self.product.title)

        clone_data = self.clone._prepare(self.product)
        clone_data.save()
        self.assertEqual(expected_title, self.product.title)
