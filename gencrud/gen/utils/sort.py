# from catalog.models import ProductFilter
# from catalog.forms import ProductFilterForm


def sort_by_params(request, object_list):
    """
    Сортировка по GET параметрам запрса
    """
    # новинки
    is_new = request.GET.get('is_new', '')
    if is_new:
        object_list = object_list.order_by(is_new)

    # по цене
    price = request.GET.get('price', '')
    if price:
        reverse = True if request.GET.get('price')[:1] == '-' else False
        object_list = list(object_list)
        object_list.sort(key=lambda o: o.get_price(), reverse=reverse)

    # по тэгам
    tag = request.GET.get('tag', '')
    if tag:
        object_list = list(object_list.filter(tags__in=tag))
    return object_list


def get_filter(request, queryset):
    pass
    # is_product_filter = ProductFilter.objects.filter(product__in=queryset).exists()
    # if is_product_filter:
    #     product_filter = ProductFilter.objects.filter(product__in=queryset)
    #     return ProductFilterForm(request.GET, queryset=product_filter)


def filter_by_param(request, queryset):
    if request.GET.keys() and list(request.GET.keys())[0]:
        product_ids = []

        for p in queryset.select_related('product').values_list('pk', flat=True):
            product_ids.append(p)

        return queryset.filter(pk__in=product_ids)

    return queryset
