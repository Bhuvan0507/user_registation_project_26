from django.shortcuts import render

# Create your views here.

from app1.models import *
from app1.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.urls import reverse

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


