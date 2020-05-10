FILEBROWSER_DIRECTORY = ''
DIRECTORY = ''
MAX_UPLOAD_SIZE = 60485760

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (2 col)', 'width': 180, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 860, 'height': '', 'opts': ''},
    'max': {'verbose_name': 'Max (12 col)', 'width': 1600, 'height': '', 'opts': ''},
}
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'large', 'max']
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
