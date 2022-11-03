from django import forms
from django.db import models
from .models import SelectedBase

class SelectedBaseForm(forms.ModelForm):
    class Meta:
        model = SelectedBase
        # fields = ['director', 'nations', 'audit']
        fields = ['director']