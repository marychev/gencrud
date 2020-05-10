from page.views import PageView
from gen.tests.page import PageMockData
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase


class PageDefaultViewTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.page = PageMockData().create()
        cls.url = cls.page.get_absolute_url()
        cls.template_name = PageView.template_name

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.page.title)

    def test_page_contains_correct_seo(self):
        self.assert_contains_seo(self.page)
