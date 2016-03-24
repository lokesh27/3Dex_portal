from django.shortcuts import render
from forms import RegForm
from content.views import index
from django.contrib.auth.decorators import login_required
from models import Student

@login_required
def reg_form(request):
    flag='update'
    try:
        instance = Student.objects.get(email_id=request.user.email)
    except:
        flag='new'
        instance=''
        pass
    if request.method == 'POST':
        if flag=='update':
            form = RegForm(request.POST or None,request.FILES,instance=instance)
        else:
            form = RegForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=request.POST.get('first_name','')
            middle_name=request.POST.get('middle_name','')
            last_name=request.POST.get('last_name','')
            email_id=request.user.email
            phone_no=request.POST.get('phone_no','')
            school_name=request.POST.get('school_name','')
            class_name=request.POST.get('class_name','')
            avatar = request.FILES['avatar']
            if flag=='update':
                instance.first_name=first_name
                instance.last_name=last_name
                instance.middle_name=middle_name
                instance.email_id=email_id
                instance.phone_no=phone_no
                instance.school_name=school_name
                instance.class_name=class_name
                instance.avatar=avatar
                instance.save()
            else:
                obj = Student(first_name=first_name,middle_name=middle_name,last_name=last_name, email_id=email_id, phone_no=phone_no,school_name=school_name,class_name=class_name,avatar=avatar)
                obj.save()
            return info(request)
        else:
            print form.errors
    else:
        form = RegForm()
    context={'form': form,'student':instance}
    return render(request,'registration.html',context)

@login_required
def info(request):
    try:
        instance = Student.objects.get(email_id=request.user.email)
    except:
        instance=''
        pass
    context={'student':instance}
    return render(request,'info.html',context)