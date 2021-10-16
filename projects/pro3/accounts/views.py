from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.

def index(request):
    return render(request,'store/index.html')

def signup(request):
    if request.method=='POST':
    
        phone=request.POST['phone']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
         
        if User.objects.filter(email=email).exists():
            return JsonResponse(
                {'success':False , 'emailerror':True},
                safe=False
            )

        else:
            user=User.objects.create_user(first_name=fname,last_name=lname,password=password,email=email)
            User_details.objects.create(phone=phone,user=user)
            
            print('user created')
            return JsonResponse(
                {'success':True},
                safe=False
            )
    else:
        return render(request,'accounts/signup.html')



def login(request):
    if request.session.has_key('email'):
        
        return redirect(index)

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)


        if user is not None:
            auth.login(request,user)
            request.session['email']=email
            return redirect(index)
        else:
            messages.info(request,'invalid credentials')
            return redirect(login)
            
    else:
            return render(request,'accounts/login.html')



def logout(request):
    auth.logout(request)
    request.session.flush() 
    return redirect('/')