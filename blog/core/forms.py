from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import entrevista

class EntrevistaForm(ModelForm):

    class Meta:
        model = entrevista
        fields = ['artista', 'fotoSmall']