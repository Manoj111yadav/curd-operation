from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


def template_view(request):
    return render(request, 'curdApp/test.html')


def add_show(request):
    if request.method  == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            ad=fm.cleaned_data['address']
            reg=User(name=nm,email=em,password=pw,address=ad)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    studd= User.objects.all()

    return render(request,'curdApp/addandshow.html',{'form':fm,'stu':studd})

def delete(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
def update(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'curdApp/updatestudent.html',{'form':fm})


