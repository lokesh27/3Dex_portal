from django import forms
from students.models import Student
from django.core.exceptions import ValidationError


class RegForm(forms.ModelForm):
    schools = (
    ('abc', 'abc'),
    ('xyz', 'xyz'),
    ('qwe', 'qwe'),
    )
    classes = ((6, 6),(7,7),(8,8),(9,9),)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    middle_name=forms.CharField(max_length=20,required = False)
    phone_no=forms.CharField(max_length=11,required=False)
    school_name=forms.ChoiceField(choices=schools,required=True)
    class_name=forms.ChoiceField(choices=classes,required=True)
    avatar=forms.ImageField(label="Upload profile picture",required=False)

    class Meta:
        model = Student
        exclude = ()

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no', None)
        if phone_no==None or phone_no=='':
            return phone_no
        try:
            int(phone_no)
            if len(phone_no)<10:
                raise ValidationError('Please enter a 10 digit phone number')
        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid phone number')
        return phone_no