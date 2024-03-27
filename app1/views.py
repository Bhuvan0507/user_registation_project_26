from django.shortcuts import render

# Create your views here.

from app1.models import *
from app1.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def registration_views(request):
    ufo=User_Form()
    pf=Profile_Form()
    D={'ufo':ufo,'pf':pf}
    if request.method =='POST'and request.FILES:
        ufd=User_Form(request.POST)
        pfd=Profile_Form(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()

            send_mail('registration','Your Registration is Successfully Done','bhuvaneswarreddy203@gmail.com',[MUFDO.email],fail_silently=False)
            return HttpResponse('Registered successfully')
        else:
            return HttpResponse('Not Registered')

        
    return render(request,'registration.html',D)






def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def user_login(request):
    if request.method =='POST':
        username=request.POST['un']
        password=request.POST['pw']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid credentials')

    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))




@login_required
def profile_display(request):
    un=request.session.get('username')
    uo=User.objects.get(username=un)
    po=Profile.objects.get(username=uo)
    d={'po':po,'uo':uo}
    return render(request,'profile_display.html',d)

@login_required
def change_password(request):
    if request.method=='POST':
        ep=request.POST['ep']
        rp=request.POST['rp']
        if ep==rp:
            username=request.session.get('username')
            uo=User.objects.get(username=username)
            uo.set_password(rp)
            uo.save()
            return HttpResponse('Password changed Successfully')
        else:
            return HttpResponse('Re-enter Password Does not matched')

    return render(request,'change_password.html')


def forget_password(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        rp=request.POST['rp']
        if pw==rp:
            uo=User.objects.filter(username=un)
            if uo:
                uo=uo[0]
                uo.set_password(rp)
                uo.save()
                return HttpResponse('Reset password successfully')
            else:
                return HttpResponse('Re-enter password does not match')
    return render(request,'forget_password.html')
    