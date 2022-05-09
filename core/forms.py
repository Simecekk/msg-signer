from django import forms
from django.forms import TextInput


class MessageForm(forms.Form):
    msg = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'message to sign ..'}))
