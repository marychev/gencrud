class MockModelData:
    def __init__(self):
        self._model = None
        self.count = 0

    @property
    def model(self):
        if self._model is not None:
            return self._model
        else:
            raise NotImplementedError(
                "Doesn't define 'model' property in '{}'".format(
                    self.__class__.__name__))

    @property
    def title(self):
        import uuid
        return 'Title {} {}'.format(self._model.__name__, uuid.uuid1().hex)

    @property
    def default_object(self):
        raise NotImplementedError(
            "Doesn't define 'default_object' property in '{}'".format(
                self.__class__.__name__))

    def create(self):
        if self.title:
            return self.model.objects.create(**self.default_object)
        else:
            raise NotImplementedError(
                "Doesn't define 'create()' method in '{}'".format(
                    self.__class__.__name__))

    def create_list(self):
        return [self.create() for _ in range(self.count)]
