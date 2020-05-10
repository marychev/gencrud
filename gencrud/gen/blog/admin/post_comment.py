from django.contrib import admin
from gen.abstract.admin import AbstractDefaultAdmin
from blog.models import Comment


@admin.register(Comment)
class BasePostCommentAdmin(AbstractDefaultAdmin):
    raw_id_fields = ('post', 'user')
    date_hierarchy = 'created'
    search_fields = ('username', 'post__title', 'text')
