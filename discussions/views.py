from django.shortcuts import render
from discussions.models import Question, Reply
from forms import QuestionForm
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'discussions/discuss.html', context)

def ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            uploader=request.user.first_name+" "+request.user.last_name
            question_text=request.POST.get('question_text','')
            import datetime
            now = datetime.datetime.now()
            obj = Question(uploader=uploader, question_text=question_text,pub_date=now)
            print obj
            obj.save()
            return index(request)
        else:
            print form.errors
    return index(request)