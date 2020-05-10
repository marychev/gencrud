from blog.views import BlogListView
from gen.tests.blog import BlogMockData, PostMockData
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase


class BlogDefaultViewTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.blog = BlogMockData().create()
        cls.post = PostMockData(cls.blog, 4).create()
        cls.url = cls.blog.get_absolute_url()
        cls.template_name = BlogListView.template_name

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.blog.title)

    def test_page_contains_correct_seo(self):
        self.assert_contains_seo(self.blog)
