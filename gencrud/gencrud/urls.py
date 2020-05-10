from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from gen.api.urls import urlpatterns as api_urlpatterns
from gen.blog.strings import APP_NAME as BLOG_APP
from gen.cart.strings import APP_NAME as CART_APP
from gen.catalog.strings import APP_NAME as CATALOG_APP
from gen.home.strings import APP_NAME as HOME_APP
from gen.order.strings import APP_NAME as ORDER_APP
from gen.page.strings import APP_NAME as PAGE_APP
from gen.search.strings import APP_NAME as SEARCH_APP
from gen.seo.init import sitemaps
from gen.seo.views import robots_txt
from gen.suit.urls import urlpatterns as admin_urlpatterns
from gen.task.strings import NAME_APP as TASK_APP
from gen.users.strings import APP_NAME as USERS_APP
from gen.utils.url import url_format, include_urls


urlpatterns = api_urlpatterns + admin_urlpatterns + [
    path('', include_urls(HOME_APP)),
    path(url_format(ORDER_APP), include_urls(ORDER_APP)),
    path(url_format(USERS_APP), include_urls(USERS_APP)),
    path(url_format(PAGE_APP), include_urls(PAGE_APP)),
    path(url_format(BLOG_APP), include_urls(BLOG_APP)),
    path(url_format(TASK_APP), include_urls(TASK_APP)),

    # modules
    path(url_format(SEARCH_APP), include_urls(SEARCH_APP, True)),
    path(url_format(CART_APP), include_urls(CART_APP, True)),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),

    # The priority has value!
    path(url_format(CATALOG_APP), include_urls(CATALOG_APP)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
                   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

