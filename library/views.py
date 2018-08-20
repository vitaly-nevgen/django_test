from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView

from library.forms import OtherAuthorForm
from library.models import Author


class MyView(TemplateView):
    template_name = 'test.html'


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

