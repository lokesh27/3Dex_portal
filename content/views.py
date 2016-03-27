from django.shortcuts import render, get_object_or_404
from .models import Lesson
from django.contrib.auth.decorators import login_required
from students.models import Student

# Create your views here.
@login_required
def index(request):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        instance=''
    lesson_list=Lesson.objects.order_by('added_date')
    context={'lesson_list':lesson_list,'student':instance}
    return render(request,'content/index.html',context)

@login_required
def detail(request, lesson_id):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        instance=''
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if lesson.allow==True:
        return render(request, 'content/detail.html', {'lesson': lesson,'student':instance})
    else:
        return index(request)