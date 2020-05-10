from django.urls import path
from .views.search import Search


urlpatterns = [
    path(r'', Search.as_view(), name='search_main'),
]

