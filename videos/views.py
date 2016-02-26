from django.shortcuts import render, get_object_or_404
from .models import Vids

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def video_list(request):
    video_list = Vids.objects.order_by('date')
    context={'video_list':video_list,'first_name':request.user.first_name}
    return render(request,'videos/video_list.html',context)