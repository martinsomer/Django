from django.forms import ModelForm
from django import forms
from .models import *

class NewThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'
