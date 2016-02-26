from django.shortcuts import render, get_object_or_404
from .models import Lesson
from news.models import News
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    news_list=News.objects.order_by('news_date')
    context={'first_name':request.user.first_name,'News':news_list}
    return render(request,'content/index.html',context)

@login_required
def detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if lesson.allow==True:
        return render(request, 'content/detail.html', {'lesson': lesson,'first_name':request.user.first_name})
    else:
        return lesson_list(request)

@login_required
def lesson_list(request):
    lesson_list = Lesson.objects.order_by('added_date')
    context={'lesson_list':lesson_list,'first_name':request.user.first_name}
    return render(request,'content/lessons.html',context)