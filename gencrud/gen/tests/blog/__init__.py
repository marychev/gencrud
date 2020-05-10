from blog.models import Blog, Post
from gen.blog.strings import APP_NAME
from gen.tests.mock_data import MockModelData


class BlogMockData(MockModelData):
    def __init__(self):
        super().__init__()
        self._model = Blog

    @property
    def title(self):
        return 'Title %s #1' % APP_NAME

    @property
    def default_object(self):
        return {
            'title': self.title,
            'is_show': True
        }


class PostMockData(MockModelData):
    def __init__(self, blog, count=100):
        super().__init__()

        self._model = Post
        self._title = 'Title {} {}'
        self.blog = blog
        self.count = count

    @property
    def default_object(self):
        return {
            'title': self.title,
            'is_show': True,
            'blog': self.blog
        }
