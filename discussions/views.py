from django.shortcuts import render
from discussions.models import Question, Reply

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'discussions/discuss.html', context)
