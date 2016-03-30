from django.shortcuts import render
from discussions.models import Question, Reply
from forms import QuestionForm,AnswerForm
import datetime
from students.models import Student
from students.views import info
# Create your views here.
def index(request):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        return info(request)
    class_name=instance.class_name
    school_name=instance.school_name
    question_list=Question.objects.raw('SELECT * FROM discussions_question WHERE for_class = %s and for_school=%s and show=1 ORDER BY pub_date DESC', [class_name,school_name])
    context = {'latest_question_list': question_list,'student':instance}
    return render(request, 'discussions/discuss.html', context)

def ask(request):
    if request.method == 'POST':
        instance=Student.objects.get(email_id=request.user.email)
        form = QuestionForm(request.POST)
        if form.is_valid():
            uploader=request.user.first_name+" "+request.user.last_name
            question_text=request.POST.get('question_text','')
            additional_info=request.POST.get('additional_info','')
            now = datetime.datetime.now()
            for_school=instance.school_name
            for_class=instance.class_name
            show=True
            obj = Question(uploader=uploader, question_text=question_text,pub_date=now,additional_info=additional_info,for_class=for_class,for_school=for_school,show=show)
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
