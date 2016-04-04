from django.shortcuts import render
from content.views import index
from django.template.response import TemplateResponse
from .models import upload
from .forms import UploadForm
from students.models import Student
from students.views import info
from content.models import MakersBoard
# Create your views here.
def list(request):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        return info
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            description=request.POST.get('description','')
            type=request.POST.get('type','')
            newsubmission = upload(file = request.FILES['file'],name=""+request.user.first_name+" "+request.user.last_name,description=description,type=type)
            newsubmission.save()
            return index(request)
    else:
        upload_list=upload.objects.all()
        form = UploadForm()
        makers_board=MakersBoard.objects.filter(show=True)
        return TemplateResponse(request,'list.html',{'form': form,'student':instance,'upload_list':upload_list,'makers':makers_board})
    return TemplateResponse(request,'list.html',{'form': form,'student':instance})


