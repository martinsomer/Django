from django.forms import ModelForm
from django import forms
from .models import *

class NewThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'

class NewReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)
