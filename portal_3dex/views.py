from django.shortcuts import render, render_to_response,RequestContext, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf
from content.views import index
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

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

@login_required
def password_change(request):
    success = None
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid(): # All validation rules pass
            form.save()
            success = True
            return HttpResponseRedirect('/password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render_to_response('login.html',{'form':form,'success':success},context_instance=RequestContext(request))

@login_required
def password_change_done(request):
    return render_to_response('password_change_done.html',{},context_instance=RequestContext(request))


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response