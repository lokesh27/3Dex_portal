from django.shortcuts import render, get_object_or_404
from .models import Lesson,Assignment
from django.http import HttpResponse
# Create your views here.
def index(request):
    lesson_list = Lesson.objects.order_by('added_date')
    context={'lesson_list':lesson_list,'first_name':request.user.first_name}
    return render(request,'content/index.html',context)

def detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'content/detail.html', {'lesson': lesson})