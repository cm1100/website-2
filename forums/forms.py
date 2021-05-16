from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class CommentForm(forms.Form):

    comment = forms.CharField(required=True,max_length=500,strip=True,min_length=3)

