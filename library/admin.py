from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from library.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'get_image')

    def get_image(self, obj):
        if not obj.image:
            return ''
        return mark_safe('<img src="{}" style="height: 200px">'.format(
            obj.image.url
        ))


admin.site.register(Book, BookAdmin)

