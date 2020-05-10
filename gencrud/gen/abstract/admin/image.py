from PIL import Image
from django.contrib import admin
from django.conf import settings
from gen.utils.thumbnail import add_watermark, __get_thumbnail__


class AbstractImageAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    readonly_fields = ('thumb',)
    search_fields = ('image_title',)
    actions = ('set_watermark',)
    list_filter = ('image_is_main',)
    list_display = ('thumb', 'image_title', 'image_description', 'image_is_main')
    list_display_links = ('thumb', 'image_title',)
    list_editable = ('image_is_main',)

    def thumb(self, obj):
        image = None
        if hasattr(obj, 'get_main_image') and hasattr(obj.get_main_image(), 'image'):
            image = obj.get_main_image().image
        elif hasattr(obj, 'get_main_image'):
            image = obj.get_main_image()
        elif hasattr(obj, 'image'):
            image = obj.image
        if image:
            return __get_thumbnail__(obj, image)
    thumb.short_description = 'Рис.'

    def set_watermark(self, request, queryset):
        """
        Help info:
        * sorl.thumbnail: >>_ python manage.py thumbnail clear_delete_all
        """
        watermark = Image.open(settings.WATERMARK_IMG, 'r')
        for query in queryset:
            if query.image:
                img_path = settings.BASE_DIR + query.image.url  # Открываем текущее изображение
                img_open = Image.open(img_path, 'r')
                print('{}: {}'.format('action `set_watermark`',
                                      add_watermark(img_open, watermark).save(img_path)))  # NOTE: print(!)
    set_watermark.short_description = 'Наложить водяной знак ``../static/images/logo.png``'

