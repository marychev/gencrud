from blog.models import Blog
from catalog.models import Catalog
from page.models import Page


def menu_limit_choices_to_parent():
    from settings_template.models import MainMenu
    return {
        'is_show': True,
        'sort__gt': 0,
        'pk__in': MainMenu.queryset_not_cloned(flat_pk=True)}


def menu_limit_choices_to_catalog():
    return {
        'is_show': True,
        'sort__gt': 0,
        'pk__in': Catalog.queryset_not_cloned(flat_pk=True)}


def menu_limit_choices_to_blog():
    return {
        'is_show': True,
        'sort__gt': 0,
        'pk__in': Blog.queryset_not_cloned(flat_pk=True)}


def menu_limit_choices_to_page():
    return {
        'is_show': True,
        'sort__gt': 0,
        'pk__in': Page.queryset_not_cloned(flat_pk=True)}
