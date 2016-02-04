from django.shortcuts import render_to_response
from django.template import RequestContext
from content.views import index

from .models import upload
from .forms import UploadForm
# Create your views here.
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newstl = upload(stlfile = request.FILES['stlfile'])
            newstl.save()

            # Redirect to the upload list after POST
            return index(request)
    else:
        form = UploadForm() # A empty, unbound form
    return render_to_response(
        'uploads/list.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


