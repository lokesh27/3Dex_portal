from django import forms
from feedback.models import Feed

class FeedbackForm(forms.ModelForm):
    name=forms.CharField(max_length=30,help_text="Your Name")
    email_id=forms.EmailField(help_text="Your Email address")
    query=forms.CharField(widget=forms.Textarea,help_text="Your Query")
    class Meta:
        model = Feed
        exclude = ()
