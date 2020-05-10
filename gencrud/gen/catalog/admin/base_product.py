from django.contrib import admin
from django.db import IntegrityError
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from catalog.models import Product, ProductImage, ProductItem, ProductParam
from gen.abstract.mixins.clone import CloneObjectMixin
from gen.abstract.admin import (
    AbstractImageInlineAdmin, AbstractPageSeoAdmin, AbstractDefaultStackedInlineAdmin,
    AbstractDefaultTabularInlineAdmin, fields_element)


class ProductResource(resources.ModelResource):
    catalog_ids = Field()

    def dehydrate_catalog_ids(self, product):
        if product.pk is not None and product.catalog.exists():
            return '%s' % list(product.catalog.all().values_list('id', flat=True))

    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = False
        # exclude = (
        # 'created', 'updated', 'author', 'tags', 'og_title', 'is_allow_comments', 'scripts', 'recommend_products')
        fields = (
            'id', 'title', 'articul', 'description', 'html', 'is_bestseller', 'is_new',
            'sort', 'slug', 'seo_title', 'seo_description', 'seo_keywords',
            'catalog_ids',
        )
        export_order = (
            'id', 'title', 'articul', 'description', 'html', 'is_bestseller', 'is_new',
            'sort', 'slug', 'seo_title', 'seo_description', 'seo_keywords',
            'catalog_ids',
        )

    def before_save_instance(self, instance, using_transactions, dry_run):
        if self.fields['articul'].get_value(instance) == '':
            instance.articul = None


class ProductParamInline(AbstractDefaultTabularInlineAdmin):
    model = ProductParam
    suit_classes = 'suit-tab suit-tab-param'


class ProductImageInline(AbstractImageInlineAdmin):
    model = ProductImage


class ProductItemInline(AbstractDefaultStackedInlineAdmin):
    model = ProductItem
    suit_classes = 'suit-tab suit-tab-price'
    raw_id_fields = ('default_price', )
    fields = (
        'name', 'text',
        ('unit', 'is_main'),
        ('price', 'price_discount'),
        'default_price',
    )


@admin.register(Product)
class BaseProductAdmin(AbstractPageSeoAdmin, ImportExportModelAdmin):
    inlines = (ProductItemInline, ProductImageInline, ProductParamInline)
    resource_class = ProductResource
    raw_id_fields = AbstractPageSeoAdmin.raw_id_fields
    readonly_fields = AbstractPageSeoAdmin.readonly_fields
    filter_horizontal = ('catalogs', 'recommend_products') + AbstractPageSeoAdmin.filter_horizontal
    list_filter = ('catalogs',) + AbstractPageSeoAdmin.list_filter
    list_display = AbstractPageSeoAdmin.list_display + ('is_bestseller', 'is_new', 'articul')
    list_display_links = AbstractPageSeoAdmin.list_display_links + ('articul', )
    list_editable = AbstractPageSeoAdmin.list_editable + ('is_bestseller', 'is_new')

    fieldsets = (
        fields_element(
            (
                'catalogs',
                'articul',
                'is_bestseller', 'is_new',
                'recommend_products',
                'layout'
             )
        ),
        AbstractPageSeoAdmin.fieldsets[0],
        AbstractPageSeoAdmin.fieldsets[2],
        AbstractPageSeoAdmin.fieldsets[3],
    )

    suit_form_tabs = (
        ('content', 'КОНТЕНТ'),
        ('price', 'ЦЕНЫ/ВАРИАНТЫ ТОВАРА'),
        ('fields', 'ПОЛЯ'),
        ('param', 'ПАРАМЕТРЫ'),
        ('seo', 'СЕО'),
        ('image', 'ФОТО'),
        ('info', 'ИНФО'),
    )

    def get_price(self, obj):
        return obj.get_price()
    get_price.short_description = 'Цена'

    def clone_object(self, request, queryset):
        [self._clone_product(request, obj) for obj in queryset]
    clone_object.short_description = CloneObjectMixin.short_description

    def _clone_product(self, request, obj):
        cache_catalogs = obj.catalogs.all()
        cache_tags = obj.tags.all()
        cache_product_items = obj.get_product_items()
        cache_product_images = obj.get_images()
        cache_product_params = obj.get_product_params()

        clone = obj
        clone.id = None
        clone.is_show = False
        clone.title = self.clone_format(clone.title)
        clone.description = self.clone_format(clone.description)
        clone.articul = self.clone_format(clone.articul)
        clone.slug = self.clone_format(clone.slug)
        clone.seo_title = self.clone_format(clone.seo_title)
        clone.seo_description = self.clone_format(clone.seo_description)
        clone.seo_keywords = self.clone_format(clone.seo_keywords)

        try:
            clone.save()

            [clone.tags.add(t) for t in cache_tags]
            [clone.catalogs.add(c) for c in cache_catalogs]

            for pi in cache_product_items:
                ProductItem(
                    product_id=clone.pk,
                    name=self.clone_format(pi.name),
                    text=pi.text,
                    unit=pi.unit,
                    price=pi.price,
                    price_discount=pi.price_discount,
                    is_main=pi.is_main,
                    default_price=pi.default_price
                ).save()

            for pi in cache_product_images:
                ProductImage(
                    product_id=clone.pk,
                    image=pi.image,
                    image_title=pi.image_title,
                    image_description=pi.image_description,
                    image_is_main=pi.image_is_main,
                ).save()

            for pp in cache_product_params:
                ProductParam(
                    product_id=clone.pk,
                    param=pp.param,
                    str_value=pp.str_value,
                    bool_value=pp.bool_value,
                ).save()

            self.clone_success(request, obj)
        except IntegrityError:
            self.clone_error(request, obj)

        return clone

    # --------------------------------------------------------------------------------------------
    # # Tree list in select !
    # -----------------------
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     field = super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    #     if db_field.title == 'parent':
    #         field.choices = [('', '---------')]
    #         for rubric in Catalog.objects.all():
    #             field.choices.append((rubric.pk, '+--'*(rubric.level) + rubric.title))
    #     return field
    # --------------------------------------------------------------------------------------------

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name in 'recommend_products':
    #
    #         print(self.get_queryset(request))
    #         current_obj = self.get_queryset(request)
    #         print(kwargs)
    #     return super(ProductAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

