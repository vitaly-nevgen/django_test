from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from rest_framework.response import Response

from library.exceptions import MyException
from library.forms import OtherAuthorForm
from library.models import Author, Book

from rest_framework import generics

from library.serializers import BookSerializer, BookCreateSerializer


class BooksApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateSerializer

        return BookSerializer

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


class BookCreateApi(generics.CreateAPIView):
    serializer_class = BookCreateSerializer


class MyView(TemplateView):
    template_name = 'test.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('my_exception'):
            raise MyException
        return super().get(request, *args, **kwargs)


class MyOtherView(TemplateView):
    template_name = 'test.html'

    def get_template_names(self):
        if self.request.GET.get('exception'):
            raise Http404()
        return super().get_template_names()

    def post(self, *args, **kwargs):
        form = OtherAuthorForm(self.request.POST)
        if form.is_valid():
            data = form.data.dict()  # <- .dict()
            if not self.request.user.is_anonymous:
                data['created_by'] = self.request.user
            Author.objects.create(**data)
        return redirect('/')

