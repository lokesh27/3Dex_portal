from django.shortcuts import render
from .models import Lesson,Assignment
from django.http import HttpResponse
# Create your views here.
def index(request):
    lesson_list = Lesson.objects.order_by('added_date')
    output = ', '.join([p.video_link for p in lesson_list])
    return HttpResponse(output)