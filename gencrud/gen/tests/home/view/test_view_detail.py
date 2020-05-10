from django.urls import reverse
from rest_framework import status
from gen.home.strings import APP_NAME
from home.views import HomePageView
from gen.tests.utils.base_default_view_test_case import BaseDefaultViewTestCase
from gen.tests.home import HomeMockData


class HomePageViewTests(BaseDefaultViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = '/'
        cls.home = HomeMockData().create()
        cls.template_name = HomePageView.template_name

    def test_view_url_by_name(self):
        response = self.client.get(self.url)
        path = response.request.get('PATH_INFO', None)
        response_reverse = self.client.get(reverse(APP_NAME))
        path_reverse = response_reverse.request.get('PATH_INFO', None)

        self.assertEquals(path, path_reverse)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_page_contains_correct_h1(self):
        self.assert_contains_h1(self.home.title)

    def test_contains_correct_seo_title(self):
        self.assert_contains_seo(self.home)
