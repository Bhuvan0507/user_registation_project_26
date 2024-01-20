from django.shortcuts import render

# Create your views here.

from app1.models import *
from app1.forms import *

def registration_views(request):
    ufo=User_Form()
    pf=Profile_Form()
    D={'ufo':ufo,'pf':pf}
    return render(request,'registration.html',D)
