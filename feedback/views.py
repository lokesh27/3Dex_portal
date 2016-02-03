from django.shortcuts import render
from forms import FeedbackForm
from content.views import index
from django.contrib.auth.decorators import login_required
from models import Feed
# Create your views here.
@login_required
def send_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name','')
            email_id=request.POST.get('email_id','')
            query=request.POST.get('query','')
            obj = Feed(name=name, email_id=email_id, query=query)
            obj.save()
            return index(request)
        else:
            print form.errors
    else:
        form = FeedbackForm()
    context={'form': form}
    return render(request,'feedback1.html',context)