from page.models import Page
from gen.page.strings import APP_NAME
from gen.tests.mock_data import MockModelData


class PageMockData(MockModelData):
    def __init__(self):
        super().__init__()
        self._model = Page

    @property
    def title(self):
        return 'Title %s #1' % APP_NAME

    @property
    def default_object(self):
        return {
            'title': self.title,
            'is_show': True
        }
