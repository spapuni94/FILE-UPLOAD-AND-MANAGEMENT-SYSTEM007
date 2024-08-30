from django import forms
from app.models import *
from django.core import validators
class CredForm(forms.Form):
    name=forms.CharField(max_length=250, required=False)
    pno =forms.CharField(max_length=250, required=False)
    email=forms.CharField(max_length=250, required=False)
    username=forms.CharField(max_length=250, required=False)
    password=forms.CharField(max_length=250, required=False)
    profile=forms.ImageField(required=False)