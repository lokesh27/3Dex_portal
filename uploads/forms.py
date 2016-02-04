from django import forms

class UploadForm(forms.Form):
    stlfile = forms.FileField(
        label='Select a file',
    )