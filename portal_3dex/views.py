from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
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
            return render(request,'invalid.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return index(request)
        else:
            return render(request,'invalid.html')


def do_logout(request):
    logout(request)
    return render(request,'login.html')
