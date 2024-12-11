from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import TODO


def signup(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        email=request.POST.get('email')
        psw=request.POST.get('pass')
        print(fnm, email,psw)
        my_user=User.objects.create_user(fnm,email,psw)
        my_user.save()
        return redirect('/login')     
    return render(request,'signup.html')


def login(request):
    return render(request,'login.html')