from django import forms

class AddDistributionForm(forms.Form):
    name = forms.CharField()
