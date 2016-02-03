from django import forms
from feedback.models import Feed

class FeedbackForm(forms.ModelForm):
    name=forms.CharField(max_length=30)
    email_id=forms.EmailField()
    query=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Feed
        exclude = ()
