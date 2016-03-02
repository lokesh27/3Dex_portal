from django.shortcuts import render
from content.views import index

from .models import upload
from .forms import UploadForm
# Create your views here.
def list(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newstl = upload(stlfile = request.FILES['stlfile'],name=""+request.user.first_name+" "+request.user.last_name)
            newstl.save()
            return index(request)
    else:
        form = UploadForm()
    return render(request,'uploads/list.html',{'form': form})


