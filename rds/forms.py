from django import forms

class AddInstanceForm(forms.Form):
    name = forms.CharField()
