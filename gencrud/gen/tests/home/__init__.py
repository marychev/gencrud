from home.models import Home
from gen.home.strings import APP_NAME
from gen.tests.mock_data import MockModelData


class HomeMockData(MockModelData):
    def __init__(self):
        super().__init__()
        self._model = Home

    @property
    def title(self):
        return 'Title %s' % APP_NAME.upper()

    @property
    def default_object(self):
        return {
            'title': self.title,
            'is_show': True
        }
