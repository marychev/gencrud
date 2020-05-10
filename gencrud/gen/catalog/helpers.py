from catalog.models import Product


class ProductHelper(Product):
    class Meta:
        abstract = True

    @staticmethod
    def random_qs(qs, count, is_random=True):
        return qs.order_by('?') if is_random else qs[:count]

    @staticmethod
    def get_new(count=100, is_random=False):
        qs = Product.objects.filter(is_show=True, is_new=True)
        return ProductHelper.random_qs(qs, count, is_random)

    @staticmethod
    def get_bestseller(count=100, is_random=False):
        qs = Product.objects.filter(is_show=True, is_bestseller=True)
        return ProductHelper.random_qs(qs, count, is_random)
