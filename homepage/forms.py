from django import forms
from homepage.models import UserInput

class inputform(forms.Form):
    text = forms.CharField(widget=forms.TextInput)