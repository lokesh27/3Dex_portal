from django import forms
from students.models import Student
from django.core.exceptions import ValidationError


class RegForm(forms.ModelForm):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    middle_name=forms.CharField(max_length=20,required = False)
    email_id=forms.EmailField()
    phone_no=forms.CharField(max_length=11)
    school_name=forms.CharField(max_length=50)
    class Meta:
        model = Student
        exclude = ()

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no', None)
        try:
            int(phone_no)
            if len(phone_no)<10:
                raise ValidationError('Please enter a 10 digit phone number')
        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid phone number')
        return phone_no