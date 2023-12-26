from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


admin.site.register(Category)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_display_links = ('title',)
    ordering = ('title',)


class ImageInline(admin.TabularInline):
    extra = 0
    fields = ('image', 'image_tag')
    model = ImageSet
    readonly_fields = ['image_tag']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'category', 'get_image',)
    list_display_links = ('title',)
    ordering = ('title',)
    readonly_fields = ('get_image',)
    search_fields = ['title']
    inlines = [
       ImageInline
    ]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80px" height="auto"')

    get_image.short_description = 'Изображение'
