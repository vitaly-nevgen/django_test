from rest_framework.response import Response

from library.models import Book, Author
from rest_framework import generics

from library.serializers import BookSerializer, BookCreateSerializer, AuthorSerializer


class AuthorListApi(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_url_kwarg = 'author_pk'


class BookListApi(generics.ListCreateAPIView):
    def get_queryset(self):
        return Book.objects.filter(
            author=self.kwargs['author_pk']
        )

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer

        return BookSerializer

    def perform_create(self, serializer):
        serializer.save(author_id=self.kwargs['author_pk'])

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            'view_exec_time': 'abcdef',
            'objects': serializer.data
        }

        return Response(response_data)


class BookDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_url_kwarg = 'book_pk'

    def get_queryset(self):
        return Book.objects.filter(
            author=self.kwargs['author_pk']
        )
