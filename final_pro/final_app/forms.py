from django import forms
from django.contrib.auth.models import User
from final_app.models import userprofileinfo


class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta(): 

        model = User
        fields = ('username','email','password')


class usrproform(forms.ModelForm):
     class Meta():
         model = userprofileinfo
         fields = ('portfolio','profile_pic')