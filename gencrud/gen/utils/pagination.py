from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


PER_PAGE = 25

'''
TODO: Add test for logic a pagination    
A: get request: /catalog/otdelochnye-materialy/?page=2
R: выбрать объекты c start_position AND end-position = start_position + PER_PAGE 
    start_position = (N_page - 1 * REP_PAGE)
'''


def get_pagination(request, object_list):
    """
    Get objects list with pagination
    :param request: request object
    :param object_list: objects list for pagination
    :return: object list {django.Paginator}
    """
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', PER_PAGE)

    paginator = Paginator(object_list, per_page)

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return object_list
