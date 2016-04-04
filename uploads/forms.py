from django import forms
from django.core.exceptions import ValidationError

class UploadForm(forms.Form):
    def validate_file_extension(value):
        import os
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.stl','.obj','.doc','.docx','.pdf','.dae','.skb','.skp']
        if not ext in valid_extensions:
            raise ValidationError(u'Please upload valid submission format')

    file = forms.FileField(label='Select a file',validators=[validate_file_extension])
    description=forms.CharField(widget=forms.Textarea)
    type=forms.CharField(max_length=50)