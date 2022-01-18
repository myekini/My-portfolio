from django import forms 
from . models import Name, Email, Message


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    sender = forms.EmailField(label=('Email'))
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

