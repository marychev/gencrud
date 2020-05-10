from django.contrib import admin
from gen.utils.thumbnail import __get_thumbnail__


class AbstractImageInlineAdmin(admin.StackedInline):
    class Meta:
        abstract = True

    extra = 0
    show_change_link = True
    suit_classes = 'suit-tab suit-tab-image'
    readonly_fields = ('thumb',)

    fields = (
        ('image', 'thumb'), 
        'image_is_main', 'image_title', 'image_description'
    )
    
    def thumb(self, obj):      
        return __get_thumbnail__(obj, obj.image)
    thumb.short_description = 'Рис.'



