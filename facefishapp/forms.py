from django import forms

class PersonForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    passcode = forms.CharField(label='passcode', max_length=100)