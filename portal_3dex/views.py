from django.shortcuts import render, render_to_response,RequestContext
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from content.views import index

def do_login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login1.html', c)


def auth_view(request):
    if request.method=='GET':
        if request.user.is_active:
            return index(request)
        else:
            context={'error':'Invalid details. Please try again'}
            return render(request,'login1.html',context)
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request)
        else:
            context={'error':'Invalid details. Please try again'}
            return render(request,'login1.html',context)

def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response