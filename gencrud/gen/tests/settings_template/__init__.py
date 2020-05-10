from settings_template.models import SettingsTemplate
from gen.tests.mock_data import MockModelData
from gen.settings_template.strings import APP_NAME
from gen.tests.home import HomeMockData
from django.contrib.sites.models import Site
from gencrud.settings import SITE_DOMAIN


class SettingsTemplateMockData(MockModelData):
    def __init__(self):
        super().__init__()
        self._model = SettingsTemplate

    @property
    def title(self):
        return 'Title %s #1' % APP_NAME

    @property
    def default_object(self):
        site = Site.objects.get_current()
        site.domain = SITE_DOMAIN
        site.save()

        return {
            'title': self.title,
            'is_included': True,
            'site': site,
            'home': HomeMockData().create()
        }
