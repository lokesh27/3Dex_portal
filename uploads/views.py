from django.shortcuts import render
from content.views import index
from django.template.response import TemplateResponse
from .models import upload
from .forms import UploadForm
# Create your views here.
def list(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid() and request.POST.get('description','')!='':
            description=request.POST['description']
            newstl = upload(stlfile = request.FILES['stlfile'],name=""+request.user.first_name+" "+request.user.last_name,description=description)
            newstl.save()
            return index(request)
    else:
        form = UploadForm()
    return TemplateResponse(request,'list.html',{'form': form})


