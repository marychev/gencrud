from django.urls import path
from page.views.page import PageView
from page.views.page_comment import PageCommentView


urlpatterns = [
    path(r'<str:slug>/', PageView.as_view(), name='page_detail'),
    path(r'comment/page/<int:page_id>/', PageCommentView.as_view(), name='page_comment'),
]

