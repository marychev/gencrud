def get_next_prev(model, obj):
    return {
        'next': get_next(model, obj),
        'prev': get_prev(model, obj)
    }


def get_next(model, obj):
    try:
        qs_param = {
            'created__gt': obj.created,
            'is_show': True
        }

        item = qs_item_product_or_post(model, obj, qs_param)
    except IndexError:
        item = None

    return item


def get_prev(model, obj):
    try:
        qs_param = {
            'created__lt': obj.created,
            'is_show': True
        }

        item = qs_item_product_or_post(model, obj, qs_param)
    except IndexError:
        item = None

    return item


def qs_item_product_or_post(model, obj, qs_param):
    if 'Product' == model.__name__:
        catalogs = obj.catalogs.filter(is_show=True, slug__isnull=False).first()
        qs_param.update({'catalogs': catalogs})
        item = model.objects.filter(**qs_param).order_by('created')[0]
    elif 'Post' == model.__name__:
        qs_param.update({'blog': obj.blog})
        item = model.objects.filter(**qs_param).order_by('created')[0]
    else:
        item = model.objects.filter(**qs_param).order_by('created')[0]

    return item
