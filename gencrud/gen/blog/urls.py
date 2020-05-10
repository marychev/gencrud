from django.urls import path

from gen.blog.strings import APP_NAME
from blog.views.blog_list import BlogListView
from blog.views.post_view import PostView


urlpatterns = [
    path(r'<str:slug>/', BlogListView.as_view(), name=APP_NAME),
    path(r'<str:blog_slug>/<str:post_slug>/', PostView.as_view(), name='blog_detail'),
]
