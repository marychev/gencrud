from django.contrib import admin
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetView
from django.urls import path, include
from filebrowser.sites import site as filebrowser_site


urlpatterns = [
    path('admin/filebrowser/', filebrowser_site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('admin/password_reset/', PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
