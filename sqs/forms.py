from django import forms

class AddMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    count = forms.IntegerField(initial=1)
