from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import upload
from .forms import UploadForm
from students.models import Student
from students.views import info
from content.models import MakersBoard
from dropdowns.models import upload_dropdown
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
            class_name=instance.class_name
            school_name=instance.school_name
            newsubmission = upload(file = request.FILES['file'],name=""+request.user.first_name+" "+request.user.last_name,description=description,type=type,school_name=school_name,class_name=class_name)
            newsubmission.save()
            return show_submissions(request)
    else:
        return show_submissions(request)

@login_required
def show_submissions(request):
    try:
        instance=Student.objects.get(email_id=request.user.email)
    except:
        return info
    upload_list=upload.objects.all()
    form = UploadForm()
    dropdowns=upload_dropdown.objects.all()
    makers_board=MakersBoard.objects.filter(show=True)
    return TemplateResponse(request,'list.html',{'form': form,'student':instance,'makers':makers_board,'uploads':upload_list,'dropdown':dropdowns})
