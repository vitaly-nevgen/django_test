from django.conf import settings
from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from library.models import Book, Author, User


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'get_image')

    def get_image(self, obj):
        if not obj.image:
            return ''
        return mark_safe('<img src="{}" style="height: 200px">'.format(
            obj.image.url
        ))


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(User)

