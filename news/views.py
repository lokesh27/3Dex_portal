from django.shortcuts import render
from models import News
from students.models import Student
from students.views import info
# Create your views here.
def display(request):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        return info(request)
    class_name=instance.class_name
    school_name=instance.school_name
    news_list=News.objects.raw('SELECT * FROM news_news WHERE for_class = %s and for_school=%s and show=1 ', [class_name,school_name])
    return render(request,'news/display.html',{'news_list': news_list})