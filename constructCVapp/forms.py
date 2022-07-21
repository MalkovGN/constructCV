from django import forms
from django.forms import ModelForm

from .models import infoCVModel


class infoCVForm(ModelForm):
    class Meta:
        model = infoCVModel
        exclude = ['user', 'fileCV']
