from django.shortcuts import render
from final_app.forms import userform,usrproform
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here

def index(request):
    return render(request,'final_app/index.html')

def register(request):

    registered = False

    if request.method == 'POST':

        usr_form = userform(data=request.POST)
        pro_form = usrproform(data=request.POST)

        if usr_form.is_valid() and pro_form.is_valid():

            user = usr_form.save()
            user.set_password(user.password)
            user.save()

            profile = pro_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(usr_form.errors,pro_form.errors)

    
    else:
        usr_form = userform()
        pro_form = usrproform()
    
    return render(request,'final_app/register.html',{'usr_form':usr_form,'pro_form':pro_form,'registered':registered})


def success(request):
    return render(request,'final_app/success.html')

@login_required
def special(request):
    return HttpResponse('successfuly loged in ')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('user not activate...yet')
        
        else:
            print('someone is tried but ......')
            print('username : {} and password {}'.format(username,password))
            return HttpResponse('try again...')
        
    else:
        return render(request,'final_app/login.html',{})
    

    
