from app1.models import * 

from django import forms

class User_Form(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        help_texts={}


class Profile_Form(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['address','Profile_pic']

