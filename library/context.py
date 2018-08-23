from library.models import Book


def get_book(request):
    return {
        'books': Book.objects.all().order_by('name')
    }
