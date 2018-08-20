from datetime import datetime

from django import forms
from django.utils import timezone

from library.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'bday')

    def clean_bday(self):
        bday = self.cleaned_data['bday']
        if bday > timezone.now():
            raise forms.ValidationError('Wrong bday')
        return bday


class OtherAuthorForm(forms.ModelForm):
    MAX_FIRST_NAME_LENGTH = 5
    MAX_LAST_NAME_LENGTH = 10

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'bday')

    def clean_bday(self):
        return '2006-10-25 14:30:59'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) > self.MAX_FIRST_NAME_LENGTH:
            raise forms.ValidationError('Invalid first_name')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) > self.MAX_LAST_NAME_LENGTH:
            raise forms.ValidationError('Invalid last_name')
        return last_name

