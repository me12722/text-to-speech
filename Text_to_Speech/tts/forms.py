from django import forms

class Mp3DetailsForm(forms.Form):
    file_name = forms.CharField(label='File Name', max_length=100)
    text = forms.CharField(widget=forms.Textarea)