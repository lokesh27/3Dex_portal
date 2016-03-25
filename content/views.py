from django.shortcuts import render, get_object_or_404
from .models import Lesson
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    lesson_list=Lesson.objects.order_by('added_date')
    context={'lesson_list':lesson_list}
    return render(request,'content/index.html',context)

@login_required
def detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if lesson.allow==True:
        return render(request, 'content/detail.html', {'lesson': lesson})
    else:
        return index(request)