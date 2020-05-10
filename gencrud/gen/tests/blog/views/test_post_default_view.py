from blog.views import PostView
from gen.tests.blog import BlogMockData, PostMockData
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase


class PostDefaultViewTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.blog = BlogMockData().create()
        cls.posts = PostMockData(cls.blog, 10).create_list()
        cls.post = cls.posts[0]
        cls.url = cls.post.get_absolute_url()
        cls.template_name = PostView.template_name

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.post.title)

    def test_page_contains_correct_seo(self):
        self.assert_contains_seo(self.post)
