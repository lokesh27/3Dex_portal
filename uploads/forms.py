from django import forms
from django.core.exceptions import ValidationError

class UploadForm(forms.Form):
    def validate_file_extension(value):
        import os
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.stl','.obj']
        if not ext in valid_extensions:
            raise ValidationError(u'Please upload valid stl or obj')

    stlfile = forms.FileField(label='Select a file',validators=[validate_file_extension])