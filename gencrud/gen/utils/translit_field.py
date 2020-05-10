import re
from transliterate import translit


def translaton_field(name):
    """Вернуть английское представление переданной строки"""
    chars = [
        ' ', '/', '.', '!', '?', '%'
        '№', 'ь', 'ъ',
        '{', '(', ')', '}', '[', ']',
    ]
    str_chars = ''.join(chars).replace(' ', '-')
    clean_name = re.sub(r'[{}]'.format(str_chars), '', name)
    return translit(clean_name, 'ru', reversed=True).lower()

    # return translit(''.join(
    #     name.replace(' ', '-')
    #         .replace('/', '-')
    #         .replace('.', '-')
    #         .replace('№', '')
    #         .replace('(', '')
    #         .replace(')', '')
    #         .replace('ь', '')
    #         .replace('[', '')
    #         .replace(']', '')
    #         .replace('!', '')
    #         .replace('?', '')
    # ), 'ru', reversed=True).lower()

