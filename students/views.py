from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(first_name=username, last_name=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/content')
    return render_to_response('students/login.html', context_instance=RequestContext(request))

@login_required(login_url='students/login/')
def main(request):
    return HttpResponse("welcome {{user.first_name}}")