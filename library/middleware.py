from django.core.exceptions import MiddlewareNotUsed
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

from library.exceptions import MyException


class TestMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        super().__init__(get_response)
        if settings.DEBUG:
            raise MiddlewareNotUsed

    def process_request(self, request):
        if request.GET.get('hello'):
            raise Http404

    def process_exception(self, request, exception):
        if isinstance(exception, MyException):
            raise Http404('Our exception')
