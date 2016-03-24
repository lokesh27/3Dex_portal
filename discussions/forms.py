from django import forms
from discussions.models import Question

class QuestionForm(forms.ModelForm):
    uploader=forms.CharField(max_length=30)
    question_text=forms.CharField(widget=forms.Textarea)
    pub_date=forms.DateTimeField()
    additional_info=forms.CharField(widget=forms.Textarea,required=False)
    class Meta:
        model = Question
        exclude = ()
