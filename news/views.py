from django.shortcuts import render
from models import News
# Create your views here.
def display(request):
    news_list=News.objects.order_by('news_date')
    return render(request,'news/display.html',{'news_list': news_list})