import datetime
import uuslug
from django.urls import include


def generate_path_year_month(instance, filename):
    """
    Формирует путь файла относительно года и месяца, чтобы множество файлов не скапливались на одном уровне.
    """
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    filename = "%s.%s" % (uuslug.slugify(".".join(filename.split('.')[:-1])), ext)
    return 'uploads/%s/%s/%s' % (today.year, today.month, filename)


def fill_get_request_param(key, list_param, list_count):
    """
    Заполнить GET запрос существующими параметрами

    :param key: {string} гет-параметр (Прим: &param=)
    :param list_param: {list} - список занчение для key (Прим: [12, 52, 89] - список IDS)
    :param list_count: {int} - кол-во занчений в списке (Прим: 3)
    :return: {string} - '&param=12&param=52&param=89'
    """
    str_list = [key+'%s' % val for val in list_param]
    val_param = "".join(str_list)
    # пустые значения для GET параметра, нужны для заполнеия пустых значений если запрос длинный(прим. фильтр)
    null_param = str(key * (list_count - len(list_param)))
    return val_param + null_param


def include_urls(app_name, is_module=False):
    return include('gen.{}.urls'.format(app_name) if is_module else '{}.urls'.format(app_name))


def url_format(app_name):
    return '{}/'.format(app_name)

