from django.shortcuts import render
from discussions.models import Question, Reply
from forms import QuestionForm,AnswerForm
import datetime
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
            additional_info=request.POST.get('additional_info','')
            now = datetime.datetime.now()
            obj = Question(uploader=uploader, question_text=question_text,pub_date=now,additional_info=additional_info)
            obj.save()
            return index(request)
        else:
            print form.errors
    return index(request)

def reply(request):
    if request.method=='POST':
        question_text=request.POST.get('question_text')
        instance=Question.objects.get(question_text=question_text)
        name=request.user.first_name+" "+request.user.last_name
        reply_text=request.POST.get('reply_text','')
        instance.reply_set.create(name=name,reply_text=reply_text)
    return  index(request)
