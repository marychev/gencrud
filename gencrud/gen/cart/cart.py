from decimal import Decimal
from gen.cart.strings import APP_NAME
from catalog.models import ProductItem, Product
from gen.utils.querystring_parser import parser
from gen.utils.price import format_price


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get(APP_NAME, [])

    def get(self):
        return self.cart

    @staticmethod
    def dict_to_list(_dict):
        return [item for _, item in _dict.items()]

    def prepare_data(self):
        errors = {}
        post_dict = parser.parse(self.request.POST.urlencode()).copy()
        total_price = Decimal(0)

        if len(post_dict) > 0 and 'id' in post_dict:
            product = Product.objects.get(id=int(post_dict['id']))

            post_dict['url'] = product.get_absolute_url()
            post_dict['main_image'] = product.get_main_image().image.url \
                if product.get_main_image() and product.get_main_image().image and product.get_main_image().image.url else None

            if 'productItems' in post_dict and isinstance(post_dict['productItems'], dict):
                post_dict['productItems'] = Cart.dict_to_list(post_dict['productItems'])

            for item in post_dict['productItems']:
                is_error, error_dict = Cart.error_no_count_product_item(item)
                if not is_error:
                    price = ProductItem.objects.get(pk=int(item['id'])).price
                    amount = Decimal(item['count']) * price

                    item.update({'totalPrice': float(amount.quantize(Decimal('0.01')))})
                    total_price += amount
                else:
                    errors.update(error_dict)

            post_dict.update({'totalPrice': float(total_price.quantize(Decimal('0.01')))})
            post_dict.update({'totalCountProductItems': self.get_total_count_product_items()})

        return post_dict if len(errors) == 0 else {'errors': errors}

    @staticmethod
    def error_no_count_product_item(product_item):
        is_error = not product_item['count'] and product_item['title']

        if not product_item['count'] and product_item['title']:
            key = 'productItem_{}'.format(product_item['id'])
            text = '{} - не установленно кол-во товара'.format(product_item['title'])
            return is_error, {key: text}

        return is_error, {}

    def exist_product(self, product_id):
        if product_id:
            for cart_product in self.cart:
                if len(cart_product) > 0 and 'id' in cart_product and int(cart_product['id']) == int(product_id):
                    return True
        return False

    def exist_product_item(self, product_item_id):
        for cart_product in self.cart:
            if len(cart_product) > 0 and 'productItems' in cart_product:
                for cpi in cart_product['productItems']:
                    if int(cpi['id']) == int(product_item_id):
                        return True
        return False

    def is_new_product(self, data):
        return len(self.cart) == 0 or not self.exist_product(data['id'])

    def add(self, data):
        if self.is_new_product(data):
            self.cart.append(data)
        else:
            self.edit(data)

        self.cart[0]['totalPrice'] = self.total_price()
        self.cart[0]['totalCountProductItems'] = self.get_total_count_product_items()

        self.save()

    def edit(self, data):
        if len(data) > 0:
            for cart_product in self.cart:
                if 'id' in cart_product and int(data['id']) == int(cart_product['id']):
                    new_product_items = []

                    for cpi in cart_product['productItems']:
                        for dpi in data['productItems']:
                            amount = Decimal(cpi['count']) * Decimal(cpi['price'])

                            if int(cpi['id']) == int(dpi['id']):
                                cpi['count'] = int(cpi['count']) + int(dpi['count'])
                                cpi['totalPrice'] = float(amount.quantize(Decimal('0.01')))
                            else:
                                new_product_items.append({
                                    'id': int(dpi['id']),
                                    'title': dpi['title'],
                                    'count': int(dpi['count']),
                                    'price': dpi['price'],
                                    'totalPrice': float(amount.quantize(Decimal('0.01')))
                                })

                    for i in new_product_items:
                        cart_product['productItems'].append(i)

    def save(self):
        self.session[APP_NAME] = self.cart
        self.session.modified = True

    def remove(self, product_item):
        for product_inx, product in enumerate(self.cart):
            if int(product['id']) == product_item.product.pk:
                for pi_inx, pi in enumerate(product['productItems']):
                    if int(pi['id']) == product_item.pk:
                        del self.cart[product_inx]['productItems'][pi_inx]
                        self.cart[product_inx]['totalCountProductItems'] = self.get_total_count_product_items() - 1
                        break

            if len(self.cart[product_inx]['productItems']) == 0:
                del self.cart[product_inx]

        self.save()

    def clear(self):
        try:
            del self.session[APP_NAME]
        except KeyError:
            pass
        self.session.modified = True

    # todo: check and use
    def get_total_price(self):
        amount = 0
        for cart_product in self.cart:
            if 'productItems' in cart_product:
                amount += sum([i['totalPrice'] for i in cart_product['productItems'] if i['totalPrice']])
        return Decimal(amount)

    def total_price(self):
        return format_price(self.get_total_price())

    def get_total_count_product_items(self):
        # for cart_product in self.cart: total_count += len(cart_product.get('productItems', {}))
        total_count = sum(len(cart_product.get('productItems', {})) for cart_product in self.cart)
        return total_count

