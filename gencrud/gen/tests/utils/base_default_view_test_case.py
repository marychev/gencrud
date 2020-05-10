from django.test import TestCase, Client
from rest_framework import status
from gencrud.settings import SITE_DOMAIN, PROTOCOL
from gen.home.views.base_home import BaseHomePageView
from gen.tests.settings_template import SettingsTemplateMockData


class BaseDefaultViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = '/'
        cls.template_name = BaseHomePageView.template_name

    def setUp(self):
        self.settings_template = SettingsTemplateMockData().create()
        self.client = Client()

    def assert_contains_h1(self, title):
        response = self.client.get(self.url)
        self.assertContains(response, '<h1')
        self.assertContains(response, '</h1')
        self.assertContains(response, title)

    def assert_contains_seo(self, object_model):
        response = self.client.get(self.url)
        self.assertContains(response, '<title>{}</title>'.format(object_model.seo_title))
        self.assertContains(response, '<meta')
        self.assertContains(response, 'content="{}"'.format(object_model.seo_description))
        self.assertContains(response, 'name="description"')
        self.assertContains(response, 'content="{}"'.format(object_model.seo_keywords))
        self.assertContains(response, 'name="keywords"')

    def check_status_code_equals(self, url, status_code=status.HTTP_200_OK):
        response = self.client.get(url)
        self.assertEquals(response.status_code, status_code)

    def test_page_status_code(self):
        self.check_status_code_equals(self.url)

    def test_meta_link_rel_canonical(self):
        response = self.client.get(self.url)
        link_canonical = self._get_meta_link_type_to('canonical')
        self.assertContains(response, link_canonical)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, self.template_name)

    def _get_meta_link_type_to(self, rel):
        response = self.client.get(self.url)
        full_path = response.wsgi_request.get_full_path()
        return '<link href="{protocol}://{domain}{path}" rel="{rel}"'.format(
            protocol=PROTOCOL, domain=SITE_DOMAIN, path=full_path, rel=rel)
