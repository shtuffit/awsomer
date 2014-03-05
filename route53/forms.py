from django import forms

class AddHostedZoneForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(required=False)

class AddRecordForm(forms.Form):
    name = forms.CharField()
